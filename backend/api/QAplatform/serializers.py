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
