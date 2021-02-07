from django.urls import path
from new_app import views

urlpatterns = [
    path('', views.hello1),
    path('hey/', views.hi),
    path('new-year/', views.is_it_newyear),
    path('fruits/', views.fruits),
    path('<str:name>/', views.name),
    path('2/<str:name>/', views.display_name2),
]
