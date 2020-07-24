from django.test import TestCase
from . import models
from django.contrib.auth.models import User
import random
import json


class TestDjango(TestCase):
    def setUp(self) -> None:
        xing = ['李', '王', '张', '刘', '陈', '杨', '赵', '黄', '周', '吴', '徐',
                '孙', '胡', '朱', '高', '林', '何', '郭', '马', '罗', '尤', '何']
        ming = ['杰', '可', '彤', '佳', '洋', '子', '旭', '旺', '祥', '屿', '田', '弼', '昊', '博', '享']
        #  加100个学生
        for i in range(1813000, 1813100):
            username = str(i) + '@qq.com'
            password = 'nkcs' + str(i)
            email = username
            id_card = str(i)
            name = random.choice(xing)
            for i in range(2):
                name = name + random.choice(ming)
            user = User.objects.create_user(username=username, password=password, email=email)
            models.UserAddition.objects.create(user=user, id_card=id_card, name=name, is_confirmed=True, occupation=2)
        #  加10个老师
        for i in range(180000, 180010):
            username = str(i) + '@qq.com'
            password = 'nkcs' + str(i)
            email = username
            id_card = str(i)
            name = random.choice(xing)
            for i in range(2):
                name = name + random.choice(ming)
            user = User.objects.create_user(username=username, password=password, email=email)
            models.UserAddition.objects.create(user=user, id_card=id_card, name=name, is_confirmed=True, occupation=1)
        #  来一个教务
        username = 'nkcs@mail.nankai.edu.cn'
        password = 'nkcs123456'
        email = username
        id_card = '000000'
        name = '教务账号'
        user = User.objects.create_user(username=username, password=password, email=email)
        models.UserAddition.objects.create(user=user, id_card=id_card, name=name, is_confirmed=True, occupation=0)
        #  添加20个房间
        for i in range(1000, 1020):
            course_id = str(i)
            name = '课程' + course_id
            desc = '这是南开大学的课程：' + name
            room = models.Room.objects.create(course_id=course_id, name=name, desc=desc)
            rd_list = []
            #  每门课随机添加30个学生
            while len(rd_list) < 30:
                i = random.randint(1813000, 1813099)
                i = str(i) + '@qq.com'
                if i not in rd_list:
                    rd_list.append(i)
            students = User.objects.filter(username__in=rd_list).all()
            for i in students:
                models.Status.objects.create(user=i, room=room)
            #  随机添加一个老师
            rd = str(random.randint(180000, 180009)) + '@qq.com'
            teacher = User.objects.filter(username=rd).first()
            models.Status.objects.create(user=teacher, room=room)
            #  随机添加一个助教
            rd = str(random.randint(1813000, 1813099)) + '@qq.com'
            assistant = User.objects.filter(username=rd).first()
            models.Status.objects.create(user=assistant, room=room, is_assistant=True)

    def test_user_model(self):
        user = list(User.objects.all())[0]
        self.assertEqual(user.username, '1813000@qq.com')

    def test_add_duplicate_course(self):
        url = 'http://localhost:8000/QAplatform/office/'
        data_duplicate = {
            'course_id': '1019',
            'name': '课程1019',
            'desc': '这是南开大学的课程：课程1019'
        }
        data_not_duplicate = {
            'course_id': '1020',
            'name': '课程1020',
            'desc': '这是南开大学的课程：课程1020'
        }
        self.client.post(url, data_not_duplicate, content_type='application/json')
        response = self.client.post(url, data_duplicate, content_type='application/json')
        dict_ret = json.loads(response.content)
        self.assertEqual(dict_ret['status'], 0)

    def test_init_view(self):
        url = 'http://localhost:8000/QAplatform/init/'
        response = self.client.get(url)
        dict_ret = json.loads(response.content)
        self.assertEqual(dict_ret['status'], 200)

    def test_register_view(self):
        url = 'http://localhost:8000/QAplatform/register/'
        data0 = {
            "username": "569107519@qq.com",
            "password": "zbc123456",
            "occupation": 2
        }
        data1 = {
            "username": "1813049@qq.com",
            "password": "zbc123456",
            "occupation": 2
        }
        data2 = {
            "username": "569107519@qq.com",
            "occupation": 2
        }
        response0 = self.client.post(url, data0, content_type='application/json')
        dict_ret0 = json.loads(response0.content)
        response1 = self.client.post(url, data1, content_type='application/json')
        dict_ret1 = json.loads(response1.content)
        response2 = self.client.post(url, data2, content_type='application/json')
        dict_ret2 = json.loads(response2.content)
        self.assertEqual(dict_ret0['status'], 200)
        self.assertEqual(dict_ret1['status'], 0)
        self.assertEqual(dict_ret2['status'], 400)
        data3 = {
            "username": "569107519@qq.com",
            "password": "zbc123456",
            "identifying_code": "STOUJJ"
        }
        response3 = self.client.put(url, data3, content_type='application/json')

    def test_login_view(self):
        url = 'http://localhost:8000/QAplatform/login/'
        data_success = {
            'username': '1813049@qq.com',
            'password': 'nkcs1813049'
        }
        data_fail0 = {
            'username': '1813049@qq.com',
            'password': 'nkcs1813000'
        }
        data_fail1 = {
            'username': '1813049@qq.com',
        }
        response_success = self.client.post(url, data_success, content_type='application/json')
        response_fail0 = self.client.post(url, data_fail0, content_type='application/json')
        response_fail1 = self.client.post(url, data_fail1, content_type='application/json')
        dict_ret_success = json.loads(response_success.content)
        dict_ret_fail0 = json.loads(response_fail0.content)
        dict_ret_fail1 = json.loads(response_fail1.content)
        self.assertEqual(dict_ret_success['status'], 200)
        self.assertEqual(dict_ret_fail0['status'], 400)
        self.assertEqual(dict_ret_fail1['status'], 400)

    def test_office_view(self):
        url = 'http://localhost:8000/QAplatform/office/'
        data = {
            'room_pk': 5
        }
        self.client.get(url)
        self.client.delete(url, data)

    def test_office_room_view(self):
        url0 = 'http://localhost:8000/QAplatform/office/room/'
        url1 = 'http://localhost:8000/QAplatform/office/room/5/'
        self.client.get(url0)
        response = self.client.get(url1)
        dict_ret = json.loads(response.content)
        self.assertEqual(dict_ret['status'], 0)

    def test_code_view(self):
        url = 'http://localhost:8000/QAplatform/code/5/'
        data = {
            'code': '#include<iostream>'
        }
        self.client.get(url)
        self.client.post(url, data, content_type='application/json')
