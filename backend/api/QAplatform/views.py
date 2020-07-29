import smtplib
import random
from email.mime.text import MIMEText
from email.header import Header
import pytz
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView, Response
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from . import serializers
from . import models
import datetime


class InitView(APIView):
    def get(self, request, *args, **kwargs):
        User.objects.all().delete()
        models.UserAddition.objects.all().delete()
        models.Room.objects.all().delete()
        models.Status.objects.all().delete()
        models.UseTime.objects.all().delete()
        models.File.objects.all().delete()

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
            print('1')
            #  随机添加一个老师
            rd = str(random.randint(180000, 180009)) + '@qq.com'
            teacher = User.objects.filter(username=rd).first()
            models.Status.objects.create(user=teacher, room=room)
            print('2')
            #  随机添加一个助教
            rd = str(random.randint(1813000, 1813099)) + '@qq.com'
            assistant = User.objects.filter(username=rd).first()
            models.Status.objects.create(user=assistant, room=room, is_assistant=True)
            print('3')
        return Response({
            'status': 200,
            'msg': '数据初始化成功'
        })


class RegisterView(APIView):
    #  用户注册发送邮箱验证码部分，用post，这时候就存了username(=email)|password|email|identifying_code
    def post(self, request, *args, **kwargs):
        occ = ['教务', '老师', '学生']
        from_addr = '569107519@qq.com'
        authorized_code = 'kiqeaizahrwebaid'
        try:
            to_addr = request.data['username']  # username和email是一样的
            password = request.data['password']
            occupation = request.data['occupation']
        except:
            return Response({
                'status': 400,
                'msg': '未输入用户名或密码'
            })
        user_obj = User.objects.filter(username=to_addr).first()
        if user_obj and user_obj.info.is_confirmed:
            return Response({
                'status': 0,
                'msg': '该邮箱已经被占用'
            })
        smtp_server = 'smtp.qq.com'
        randomLetters = '234567890QWEASDZXCRTYFGHVBNJKLUIO'
        code = ''
        for i in range(6):
            code = code + random.choice(randomLetters)
        msg = MIMEText('[QAplatform]验证码:' + code + '你正在注册成为QAplatform用户，感谢您的支持！', 'plain', 'utf-8')
        msg['From'] = Header(from_addr)
        msg['To'] = Header(to_addr)
        msg['Subject'] = Header('计发客count hair')
        server = smtplib.SMTP_SSL(smtp_server)
        server.connect(smtp_server, 465)
        server.login(from_addr, authorized_code)
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.quit()
        #  两种情况：1.用户在数据库里面存在，并不是第一次发邮箱，处于 is_confirmed = False,
        #          2.用户在数据库里面不存在，第一次发邮箱，这时需要新建用户，并且设置email
        user_obj = User.objects.filter(username=to_addr).first()
        if user_obj:
            models.UserAddition.objects.filter(user=user_obj).update(identifying_code=code)
        else:
            user = User.objects.create_user(username=to_addr, password=password, email=to_addr)
            models.UserAddition.objects.create(user=user, identifying_code=code, occupation=occupation)
        return Response({
            'status': 200,
            'msg': '邮箱验证码发送成功'
        })

    #  用户注册邮箱的发送验证码部分，进行提交
    def put(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        identifying_code = request.data.get('identifying_code')
        user_obj = User.objects.filter(username=username).first()
        if not user_obj:
            return Response({
                'status': 400,
                'msg': '注册失败，是否没有请求发送邮箱验证码'
            })
        if identifying_code != user_obj.info.identifying_code:
            return Response({
                'status': 0,
                'msg': '注册失败，邮箱验证码输入错误'
            })
        obj = User.objects.get(username=username)
        obj.set_password(password)
        obj.save()
        models.UserAddition.objects.filter(user=user_obj).update(is_confirmed=True)
        payload = jwt_payload_handler(user_obj)
        token = jwt_encode_handler(payload)
        return Response({
            'status': 200,
            'msg': '注册成功',
            'token': token,
            'occupation': user_obj.info.occupation,
            'user_pk': user_obj.pk
        })


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            user = User.objects.filter(username=username).first()
            if user and user.check_password(password) and user.info.is_confirmed:
                #  将来增加职业：教务处人员、教师、学生
                #  手动签发token： user ==> payload ==> token
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                return Response({
                    'status': 200,
                    'msg': '登陆成功',
                    'token': token,
                    'occupation': user.info.occupation,
                    'user_pk': user.pk
                })
            return Response({
                'status': 400,
                'msg': '用户名或密码错误'
            })
        except:
            return Response({
                'status': 400,
                'msg': '登陆异常'
            })


class UserDetail(APIView):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({
            'data': serializers.UserSerializer(request.user.info).data
        })

    def post(self, request, *args, **kwargs):
        if request.data.get('id_card'):
            models.UserAddition.objects.filter(user=request.user).update(id_card=request.data.get('id_card'))
        if request.data.get('name'):
            models.UserAddition.objects.filter(user=request.user).update(name=request.data.get('name'))
        return Response({
            'status': 200,
            'msg': '信息修改成功'
        })


#  主界面的view，老师和学生可以看到自己的所有课（给老师和学生用）
class HomeView(APIView):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    # 老师和学生得到自己的课
    def get(self, request, *args, **kwargs):
        rooms = models.Room.objects.filter(user=request.user)
        status = models.Status.objects.filter(user=request.user)
        if rooms:
            return Response({
                'status': 200,
                'msg': 'successfully return the data of room',
                'room_data': serializers.RoomModelSerializer(rooms, many=True).data,
                'is_assistant_data': serializers.StatusModelSerializer(status, many=True).data
            })
        return Response({
            'status': 0,
            'msg': 'no data return'
        })

    # 老师可以指定某一个课的时间
    def post(self, request, *args, **kwargs):
        if request.user.info.occupation != 1:
            return Response({
                'status': 0,
                'msg': '身份信息校验有误'
            })
        try:
            start_time = request.data.get('start_time')
            end_time = request.data.get('end_time')
        except:
            return Response({
                'status': 0,
                'msg': '输入数据格式错误'
            })
        cmp_start = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        cmp_end = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        for item in request.user.rooms.all():
            for time_item in item.use_time.all():
                if not (cmp_end <= time_item.start_time or cmp_start >= time_item.end_time):
                    return Response({
                        'status': 0,
                        'msg': '当前时间段已经被占用，不可用'
                    })
        room_sepcified = models.Room.objects.filter(pk=request.data.get('room_pk')).first()
        interval = models.UseTime.objects.create(start_time=start_time, end_time=end_time, room=room_sepcified)
        return Response({
            'status': 200,
            'msg': '创建成功',
            'data': {
                'start_time': interval.start_time,
                'end_time': interval.end_time
            }
        })

    # 老师可以删除某一个课的时间,传过来时间段的主键就行
    def delete(self, request, *args, **kwargs):
        if models.UseTime.objects.filter(pk=request.data.get('time_pk')).delete():
            return Response({
                'status': 200,
                'msg': 'successfully delete'
            })
        return Response()


#  教务处的view,操作有：对课程（房间）的增删改查，
class OfficeHomeView(APIView):
    #  主界面得到所有的房间信息
    def get(self, request, *args, **kwargs):
        rooms = models.Room.objects.all()
        return Response({
            'data': serializers.OfficeHomeSerializer(rooms, many=True).data
        })

    #  主界面可以添加房间
    def post(self, request, *args, **kwargs):
        try:
            room_serializer = serializers.OfficeHomeSerializer(data=request.data)
            room_serializer.is_valid(raise_exception=True)
            room_obj = room_serializer.save()
            return Response({
                'status': 200,
                'msg': 'successfully add room',
                'pk': room_obj.pk
            })
        except ValidationError as e:
            return Response({
                'status': 0,
                'msg': '课程号为' + request.data.get('course_id') + '的课程已经存在，不能重复添加'
            })

    #  主界面可以删除房间,只需要知道房间的pk就行
    def delete(self, request, *args, **kwargs):
        models.Room.objects.filter(pk=request.data.get('room_pk')).delete()
        return Response({
            'status': 200,
            'msg': 'successfully delete'
        })


#  教务处对于某一个课程可以进行老师、助教、学生的增删改查
class OfficeRoomView(APIView):
    #  对一个特定的房间查询它的老师、助教、学生的信息（当前所有的老师、助教、学生以及可供选择的老师、学生、助教信息）
    def get(self, request, *args, **kwargs):
        try:
            room = models.Room.objects.get(pk=kwargs.get('pk'))
        except:
            return Response({
                'status': 0,
                'msg': 'no data'
            })
        return Response({
            'status': 200,
            'msg': 'successfully return the data of the room: %s' % room.pk,
            'data': serializers.OfficeRoomSerializer(room).data
        })

    #  可以增加老师、助教、学生,只需要知道pk就行
    def post(self, request, *args, **kwargs):
        room = models.Room.objects.filter(pk=kwargs.get('pk')).first()
        choice = request.data.get('choice')
        if choice == 3:
            # 更改描述
            desc = request.data.get('desc')
            room.desc = desc
            room.save()
            return Response({
                'room_pk': room.pk,
                'desc': room.desc
            })
        elif choice == 0:
            # 增加老师
            teacher_pks = request.data.get('pks')
            for pk in teacher_pks:
                teacher = User.objects.filter(pk=pk).first()
                models.Status.objects.create(user=teacher, room=room)
        else:
            student_pks = request.data.get('pks')
            for pk in student_pks:
                student = User.objects.filter(pk=pk).first()
                if choice == 1:
                    # 增加助教
                    models.Status.objects.create(user=student, room=room, is_assistant=True)
                elif choice == 2:
                    # 增加学生
                    models.Status.objects.create(user=student, room=room)
        return Response({
            'status': 200,
            'msg': '增加成功'
        })


    #  可以删除老师、助教、学生，只需要知道pk就行
    def delete(self, request, *args, **kwargs):
        room = models.Room.objects.filter(pk=kwargs.get('pk')).first()
        for pk in request.data.get('pks'):
            user_del = User.objects.filter(pk=pk).first()
            room.user.remove(user_del)
        return Response({
            'status': 200,
            'msg': '删除成功'
        })


#  上传图片
class OfficeUpLoadImg(APIView):
    def post(self, request, *args, **kwargs):
        ret = models.Room.objects.filter(pk=kwargs.get('pk')).first()
        ret.img = request.FILES['file']
        ret.save()
        return Response({
            'status': 200,
            'msg': '图片上传成功'
        })


#  房间内的消息记录
class MsgView(APIView):
    def get(self, request, *args, **kwargs):
        room = models.Room.objects.filter(pk=kwargs.get('room_pk')).first()
        messages = models.Message.objects.filter(room=room).all()
        return Response({
            'data': serializers.MessageSerializer(messages, many=True).data
        })

    def post(self, request, *agrs, **kwargs):
        try:
            user = User.objects.filter(pk=request.data.get('user_pk')).first()
            room = models.Room.objects.filter(pk=kwargs.get('room_pk')).first()
            msg = request.data.get('msg')
            if user and room and msg:
                models.Message.objects.create(msg=msg, user=user, room=room)
                return Response({
                    'status': 200,
                    'msg': '消息发送成功'
                })
        except:
            return Response({
                'status': 0,
                'msg': '数据有误'
            })


#  代码编辑器
class CodeView(APIView):
    def get(self ,request, *args, **kwargs):
        room = models.Room.objects.filter(pk=kwargs.get('room_pk')).first()
        return Response({
            'data': serializers.CodeSerializer(room).data
        })

    def post(self, request, *args, **kwargs):
        code = request.data.get('code')
        models.Room.objects.filter(pk=kwargs.get('room_pk')).update(code=code)
        return Response()

