import smtplib
import random
from email.mime.text import MIMEText
from email.header import Header
from rest_framework.views import APIView, Response
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from . import serializers
from . import models


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
        randomLetters = '234567890qwertyuiopasdfghjkzxcvbnmQWEASDZXCRTYFGHVBNJKLUIO'
        code = ''
        for i in range(6):
            code = code + random.choice(randomLetters)
        msg = MIMEText('你正在注册...验证码：' + code, 'plain', 'utf-8')
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
            'occupation': user_obj.info.occupation
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
                    'occupation': user.info.occupation
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
            'pk': request.user.pk,
            'username': request.user.username,
            'name': models.UserAddition.objects.filter(user=request.user).first().name,
            'is_confirmed': models.UserAddition.objects.filter(user=request.user).first().is_confirmed,
            'occupation': request.user.info.occupation
        })
