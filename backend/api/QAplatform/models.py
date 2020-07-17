from django.db import models
from django.contrib.auth.models import User


#  使用Django自带的User，user作为一对一的外键，作为信息的补充
class UserAddition(models.Model):
    OCCUPATION_CHOICES = [
        [0, '教务'],
        [1, '老师'],
        [2, '学生']
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='info')
    identifying_code = models.CharField(max_length=10)
    id_card = models.CharField(max_length=10)
    name = models.CharField(max_length=12, default='未命名')
    img = models.ImageField(upload_to='img', default='img/default.jpg')
    is_confirmed = models.BooleanField(default=False)
    occupation = models.IntegerField(choices=OCCUPATION_CHOICES, default=2)

    @property
    def user_info(self):
        return {
            'pk': self.user.pk,
            'username': self.user.username
        }


#  课程房间
class Room(models.Model):
    course_id = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    desc = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='img', default='img/default.png')
    user = models.ManyToManyField(User, related_name='rooms', through='Status')

    @property
    def use_time_list(self):
        list = []
        for item in self.use_time.only('start_time', 'end_time'):
            temp = {
                'time_pk': item.pk,
                'start_time': str(item.start_time),
                'end_time': str(item.end_time)
            }
            list.append(temp)
        return list

    @property
    def file_list(self):
        list = []
        for item in self.file.only('file'):
            temp = {
                'file': str(item.file)
            }
            list.append(temp)
        return list

    @property
    def user_list(self):
        user_info = self.user.values('pk', 'info__id_card', 'info__name', 'info__occupation', 'status__is_assistant')
        list = {
            'teachers': [],
            'assistants': [],
            'students': [],
            'ex_teachers': [],
            'ex_assistants': [],
            'ex_students': []
        }
        pks = []
        #  课程的老师学生助教信息
        for item in user_info:
            temp = {
                'pk': item['pk'],
                'id_card': item['info__id_card'],
                'name': item['info__name'],
            }
            pks.append(item['pk'])
            if item['info__occupation'] == 1:  # teacher
                list['teachers'].append(temp)
            if item['info__occupation'] == 2:  # student
                if item['status__is_assistant']:
                    list['assistants'].append(temp)
                else:
                    list['students'].append(temp)
        #  不在课程的老师学生助教信息（可供前端选择进行增删）
        for item in UserAddition.objects.all():
            if item.user.pk in pks:
                continue
            temp = {
                'pk': item.user.pk,
                'id_card': item.id_card,
                'name': item.name
            }
            if item.occupation == 1:  # teacher
                list['ex_teachers'].append(temp)
            if item.occupation == 2:  # student
                list['ex_students'].append(temp)
                list['ex_assistants'].append(temp)
        return list


class Status(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='status')
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    #  用户和房间多对多关系的额外字段
    is_assistant = models.BooleanField(default=False)


class UseTime(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    room = models.ForeignKey(to='Room', on_delete=models.CASCADE, related_name='use_time')


class File(models.Model):
    file = models.FileField(upload_to='file')
    room = models.ForeignKey(to='Room', on_delete=models.CASCADE, related_name='file')

