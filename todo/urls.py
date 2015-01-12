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
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^$', 'todo_list.views.index', name='index'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)