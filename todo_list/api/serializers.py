from rest_framework import serializers
from todo_list.models import User, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

class TaskSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Task