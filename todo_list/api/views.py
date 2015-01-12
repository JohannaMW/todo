from django.views.decorators.csrf import csrf_exempt
from todo_list.models import User, Task
from rest_framework import viewsets
from todo_list.api.serializers import UserSerializer, TaskSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @csrf_exempt
    def pre_save(self, obj):
        user = self.request.user
        obj.owner = user