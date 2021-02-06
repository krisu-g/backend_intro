from django.urls import path

from . import views

app_name = 'links'

urlpatterns = [
    path('first/', views.first, name='first'),
    path('second/', views.second, name='second'),
    path('third/<str:x>', views.third, name='third'),
]