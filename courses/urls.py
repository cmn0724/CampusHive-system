# courses/urls.py
from django.urls import path
from .views import CourseListView , CourseCreateView
# from . import views

app_name = 'courses'

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('create/', CourseCreateView.as_view(), name='course_create'), 
]