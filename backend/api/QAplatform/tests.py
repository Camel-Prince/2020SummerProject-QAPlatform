from django.test import TestCase
from django.contrib.auth.models import User
import random
from . import models

class Test(TestCase):
    def setUp(self):
        print('##########开始初始化数据库##########')
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
            models.Status.objects.create(user=teacher ,room=room)
            #  随机添加一个助教
            rd = str(random.randint(1813000, 1813099)) + '@qq.com'
            assistant = User.objects.filter(username=rd).first()
            models.Status.objects.create(user=assistant, room=room, is_assistant=True)
        print('##########数据库初始化完成##########')

    def test_model(self):
        print('##########开始测试model##########')
        students = User.objects.filter(info__occupation=2).all()
        for i in range(100):
            self.assertEqual(students[i].username, str(1813000 + i) + '@qq.com')
        print('##########model测试完成##########')
