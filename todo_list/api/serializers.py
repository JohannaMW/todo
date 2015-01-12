from rest_framework import serializers
from todo_list.models import User, Task

class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField('get_task_owner')

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'tasks')
        write_only_fields = ('password',)

    def get_task_owner(self, obj):
        return Task.objects.filter(owner=obj).values()

class TaskSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Task