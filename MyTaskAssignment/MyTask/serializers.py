
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'category', 'create_time', 'updated_time']
        read_only_fields = ['id', 'create_time', 'updated_time']
