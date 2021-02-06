from django.urls import path

from . import views


app_name = 'form_app2'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('task-list/', views.task_list, name='task_list'),
]
