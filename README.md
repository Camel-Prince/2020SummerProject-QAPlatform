# QAPlatform

## 配置环境

打开你的命令行界面，找到一个目录位置，拉取仓库

```bash
git clone https://se.jisuanke.com/course/python38.git
```

## 如果是Docker Toolbox需要先启动

docker-machine start

拉取完成后进入目录

```bash
cd python38
```

进行构建（注意最后一个表示当前位置的 `.` 不能丢了）

```bash
docker build -t "python:38" .
```

## 进入环境

首次进入：

```bash
docker run -it -p 8000:8000 -v `pwd`:/code --name QAplatform python:38
```

## 如果是Docker Toolbox需在VM中设置共享文件夹

之后进入

```bash
docker start QAplatform
docker exec -it QAplatform /bin/bash
```

## 创建数据库

```bash
docker run --name mariadb -e MYSQL_ROOT_PASSWORD=root-password -d mariadb

docker exec -it mariadb /bin/bash

mysql -uroot -proot-password

create database QAplatform default character set utf8 collate utf8_unicode_ci;
```

# 启动guestbook进入
```bash
docker start QAplatform
docker exec -it QAplatform /bin/bash
pipenv install django
pipenv install djangorestframework
pipenb install mysqlclient
pipenv install django-cors-headers
pipenv shell
```
# 上述环境配置完成后
```bash
启动docker中mysql服务

docker start maiadb

docker exec -it mariadb /bin/bash

mysql -uroot -proot-password
```
启动guestbook
```bash
docker start QAplatform

docker exec -it QAplatform /bin/bash

pipenv shell

cd code
```
数据库迁移
```bash
./manage.py migrate

./manage.py createsuperuser

./manage.py makemigrations QAplatform

./manage.py migrate QAplatform
```
启动
```bash
./manage.py runserver 0:8000
```
进入项目文件中的fontend文件夹
 
npm run serve

# 完成上述步骤后可观察到项目最终成功
留言，注册，登录，点赞等功能均已实现
点赞等功能需要发送请求，当前页面的数据有时需要刷新页面才可以观察到变化 大部分时间均可以准确显示





