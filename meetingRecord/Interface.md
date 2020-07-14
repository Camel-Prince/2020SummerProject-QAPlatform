# 后端接口文档

### 1.注册相关接口 
#### 请求地址
```url
http://localhost:8000/QAplatform/register/
```
#### 请求方式
注册分为两步：获取邮箱验证码、进行注册（获取验证码用post、进行注册用put）
```
post/put
```

#### 请求数据
获取邮箱验证码：
```json
{
    "username": "1258293645@qq.com",
    "password": "zbc123456",
    "occupation": 2
}
```
进行注册:
```json
{
    "username": "569107519@qq.com",
    "password": "zbc123456",
    "identifying_code": "xLfiRG"
}
```
#### 接口返回
获取验证码：
```json
{
    "status": 200,
    "msg": "邮箱验证码发送成功"
}
```
进行注册：
```json
邮箱验证码输入错误：
{
    "status": 0,
    "msg": "注册失败，邮箱验证码输入错误"
}
邮箱验证码输入正确：
{
    "status": 200,
    "msg": "注册成功",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6IjU2OTEwNzUxOUBxcS5jb20iLCJleHAiOjE1OTQ2NjUxNjgsImVtYWlsIjoiNTY5MTA3NTE5QHFxLmNvbSJ9.xD7knuYKzLZxKwKud7JExgQorIFAh-zN6WhVvqa8hFo",
    "occupation": 2
}
成功注册后默认是登录状态，因此返回相应的token(由djangorestframework-jwt签发和校验)
```
### 2.登陆相关接口
#### 请求地址
```url
http://localhost:8000/QAplatform/login/
```
#### 请求方式
```
post
```
#### 请求数据
```json
{
    "username": "569107519@qq.com",
    "password": "zbc123456"
}
```
#### 接口返回
```json
正确登录：
{
    "status": 200,
    "msg": "登陆成功",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6IjU2OTEwNzUxOUBxcS5jb20iLCJleHAiOjE1OTQ2NTg0NzYsImVtYWlsIjoiNTY5MTA3NTE5QHFxLmNvbSJ9.FF7i1GW3mlmW8TYzg9xEXu_ojZjXIXE1OPar5hEaHVQ",
    "occupation": 2
}
错误登录：
{
    "status": 400,
    "msg": "用户名或密码错误"
}
```
### 3.用户个人信息查看接口
#### 请求地址
```url
http://localhost:8000/QAplatform/center/
```
#### 请求方式
```
get
```
#### 请求参数
Headers里面添加：
```
KEY: Authorization
```
```
VALUE: jwt eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6IjU2OTEwNzUxOUBxcS5jb20iLCJleHAiOjE1OTQ2NDA4MjIsImVtYWlsIjoiNTY5MTA3NTE5QHFxLmNvbSJ9.DyILu5UFWJKrSngJ59DUvtgbXQntbokaKph_GFi6a5s
```
#### 接口返回
```json
正确返回
{
    "username": "569107519@qq.com",
    "email": "569107519@qq.com",
    "data": {
        "id_card": "1813049",
        "name": "0",
        "img": "/media/img/default.jpg",
        "occupation": 2
    }
}
token错误
{
    "detail": "Error decoding signature."
}
token过期
{
    "detail": "token expire."
}
```
### 4.老师/学生主界面房间信息查看接口
#### 请求地址
```url
http://localhost:8000/QAplatform/home/
```
#### 请求方式
```
get/post/delete
```
#### 请求数据
```html
三种请求方式都需要在Headers里面添加token
KEY:Authorization
VALUE:jwt eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6IjU2OTEwNzUxOUBxcS5jb20iLCJleHAiOjE1OTQ2NDA4MjIsImVtYWlsIjoiNTY5MTA3NTE5QHFxLmNvbSJ9.DyILu5UFWJKrSngJ59DUvtgbXQntbokaKph_GFi6a5s
```
```json
get 不需要请求数据，后台通过token校验身份
post
{
    "room_pk": 2,
    "start_time": "2000-01-09 12:00:00",
    "end_time": "2000-01-09 12:00:00"
}
delete
{
    "time_pk": 2
}
```
#### 接口返回
```json
get返回当前的老师/助教/同学相关联的课程房间信息
{
    "status": 200,
    "msg": "successfully return the data of room",
    "room_data": [
        {
            "pk": 1,
            "course_id": "123",
            "name": "java",
            "desc": "",
            "img": "/media/img/1.png",
            "use_time_list": [
                {
                    "time_pk": 8,
                    "start_time": "2030-07-12 16:25:00+00:00",
                    "end_time": "2030-07-12 16:25:00+00:00"
                }
            ],
            "file_list": []
        },
        {
            "pk": 2,
            "course_id": "456",
            "name": "cpp",
            "desc": "",
            "img": "/media/img/2.png",
            "use_time_list": [
                {
                    "time_pk": 3,
                    "start_time": "2020-07-12 16:25:00+00:00",
                    "end_time": "2020-07-12 16:25:00+00:00"
                },
                {
                    "time_pk": 9,
                    "start_time": "2000-01-09 04:00:00+00:00",
                    "end_time": "2000-01-09 04:00:00+00:00"
                },
                {
                    "time_pk": 10,
                    "start_time": "2000-01-09 04:00:00+00:00",
                    "end_time": "2000-01-09 04:00:00+00:00"
                }
            ],
            "file_list": [
                {
                    "file": "file/3_计发客.pdf"
                }
            ]
        },
        {
            "pk": 3,
            "course_id": "789",
            "name": "python",
            "desc": "",
            "img": "/media/img/62.JPG",
            "use_time_list": [
                {
                    "time_pk": 4,
                    "start_time": "2020-07-12 16:25:00+00:00",
                    "end_time": "2020-07-12 16:25:00+00:00"
                },
                {
                    "time_pk": 5,
                    "start_time": "2020-07-12 16:25:00+00:00",
                    "end_time": "2020-07-12 16:25:00+00:00"
                },
                {
                    "time_pk": 6,
                    "start_time": "2020-07-12 16:25:00+00:00",
                    "end_time": "2020-07-12 16:25:00+00:00"
                },
                {
                    "time_pk": 7,
                    "start_time": "2020-07-12 16:25:00+00:00",
                    "end_time": "2020-07-12 16:25:00+00:00"
                }
            ],
            "file_list": []
        },
        {
            "pk": 4,
            "course_id": "1234",
            "name": "algorithm",
            "desc": null,
            "img": "/media/img/default.png",
            "use_time_list": [],
            "file_list": []
        }
    ],
    "is_assistant_data": [
        {
            "room": 1,
            "is_assistant": false
        },
        {
            "room": 2,
            "is_assistant": false
        },
        {
            "room": 3,
            "is_assistant": true
        },
        {
            "room": 4,
            "is_assistant": false
        }
    ]
}
post成功
{
    "status": 200,
    "msg": "创建成功",
    "data": {
        "start_time": "2000-01-09 12:00:00",
        "end_time": "2000-01-09 12:00:00"
    }
}
post失败(输入的datetime类数据格式错误)
{
    "status": 0,
    "msg": "输入数据格式错误"
}
delete成功
{
    "status": 200,
    "msg": "successfully delete"
}
```
### 5.教务处主界面查看所有房间、增加删除房间
#### 请求地址
```url
http://localhost:8000/QAplatform/office/
```
#### 请求方式
```
get/post/delete
```
#### 请求参数
```json
get 携带token即可，后台进行身份校验
post
{
    "course_id": "485",
    "name": "java"
}
delete
{
    "room_pk": 4
}
```

#### 接口返回
```json
get
{
    "data": [
        {
            "pk": 1,
            "course_id": "123",
            "name": "java",
            "img": "/media/img/1.png"
        },
        {
            "pk": 2,
            "course_id": "456",
            "name": "cpp",
            "img": "/media/img/2.png"
        },
        {
            "pk": 3,
            "course_id": "789",
            "name": "python",
            "img": "/media/img/62.JPG"
        },
        {
            "pk": 4,
            "course_id": "1234",
            "name": "algorithm",
            "img": "/media/img/default.png"
        }
    ]
}
post成功
{
    "status": 200,
    "msg": "successfully add room",
    "pk": 6
}
post失败
{
    "course_id": {
        "status": "0",
        "msg": "课程号为485的课程已经存在，不能重复添加"
    }
}
delete
{
    "status": 200,
    "msg": "successfully delete"
}
```
### 6.教务处查看某一房间信息
#### 请求地址
```url
http://localhost:8000/QAplatform/office/room/(room_pk)/
http://localhost:8000/QAplatform/office/room/1/
```
#### 请求方式
```
get
```
#### 请求参数
get 携带token即可，后台进行身份校验
#### 接口返回
```json
get
{
    "status": 200,
    "msg": "successfully return the data of the room: 3",
    "data": {
        "pk": 3,
        "course_id": "789",
        "name": "python",
        "desc": "",
        "user_list": {
            "teachers": [],
            "assistants": [
                {
                    "pk": 2,
                    "id_card": "1813049",
                    "name": "0"
                }
            ],
            "students": [],
            "ex_teachers": [],
            "ex_assistants": [],
            "ex_students": []
        }
    }
}
```
持续更新中。。。。


