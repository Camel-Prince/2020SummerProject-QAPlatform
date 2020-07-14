from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from . import models


class RoomModelSerializer(ModelSerializer):
    class Meta:
        model = models.Room
        fields = ('pk', 'course_id', 'name', 'desc', 'img', 'use_time_list', 'file_list')


class StatusModelSerializer(ModelSerializer):
    class Meta:
        model = models.Status
        fields = ('room', 'is_assistant')


class OfficeHomeSerializer(ModelSerializer):
    class Meta:
        model = models.Room
        fields = ('pk', 'course_id', 'name', 'img')

    def validate_course_id(self, value):
        if models.Room.objects.filter(course_id=value):
            raise ValidationError({
                'status': 0,
                'msg': '课程号为' + value + '的课程已经存在，不能重复添加'
            })
        return value


class OfficeRoomSerializer(ModelSerializer):
    class Meta:
        model = models.Room
        fields = ('pk', 'course_id', 'name', 'desc', 'img', 'user_list')
