from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from todo import settings
from django.conf.urls.static import static
from todo_list.api.views import UserViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'tasks', TaskViewSet, base_name='tasks')

urlpatterns = patterns('',
    # REST Routes
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^$', 'todo_list.views.home', name='home'),
    url(r'^profile/', 'todo_list.views.profile', name='profile'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #AJAX CALLS
    url(r'^get_user/', 'todo_list.views.get_user', name='get_user'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)