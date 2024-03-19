from rest_framework import routers
from courses import views
from django.urls import path, include

r = routers.DefaultRouter()
r.register('categories', views.CategoryViewSet, basename='categories')
r.register('course', views.CourseViewset, basename='course')
r.register('lessons', views.lessonViewSet, basename='lessons')
r.register('users', views.UserViewSet, basename='user')

urlpatterns = [
    path("", include(r.urls))
]
