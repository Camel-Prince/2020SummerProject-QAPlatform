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

首次进入：pwd跟换为本地仓库的地址

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

# 启动QAplatform进入
```bash
docker start QAplatform
docker exec -it QAplatform /bin/bash
pipenv install django
pipenv install djangorestframework
pipenv install djangorestframework-jwt
pipenv install mysqlclient
pipenv install django-cors-headers
pipenv install Pillow
pipenv shell
```
# 上述环境配置完成后
```bash
启动docker中mysql服务

docker start mariadb

docker exec -it mariadb /bin/bash

mysql -uroot -proot-password
```
启动QAplatform
```bash
docker start QAplatform

docker exec -it QAplatform /bin/bash

pipenv shell

```
数据库迁移
```bash
cd backend

cd api

./manage.py migrate(or python manage.py migrate)

./manage.py createsuperuser(or python manage.py createsuperuser)

./manage.py makemigrations QAplatform(or python manage.py makemigrations)

./manage.py migrate QAplatform(or python manage.py migrate)
```
启动
```bash
./manage.py runserver 0:8000(or python manage.py runserver 0.0.0.0:8000)
```
进入项目文件中的fontend文件夹
 
npm run serve

### 直播docker环境配置
---
docker pull alfg/nginx-rtmp  (建议拉取国内镜像)
docker run -it -p 1935:1935 -p 8080:80 --rm alfg/nginx-rtmp
---







