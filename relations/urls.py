from django.urls import path

from . import views


app_name = 'relations'

urlpatterns = [
    path('', views.index, name='index'),
]
