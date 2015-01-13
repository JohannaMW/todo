from django.core import serializers
from django.shortcuts import render, HttpResponse
from models import Task, User



def index(request):
    tasks = Task.objects.filter(owner=request.user).order_by('due', 'title')
    return render(request, "index.html",
        {'tasks': tasks})

def get_user(request):
    user = User.objects.get(email=request.user.email)
    data = serializers.serialize('json', [user])
    return HttpResponse(data, content_type='application/json')