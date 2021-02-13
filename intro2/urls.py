from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hello1/', views.hello1),
    # path('abc/', views.hello2),
    # path('hello3/', views.hello3),
    # path('new/', views.new1),
    path('new_app/', include('new_app.urls')),
    path('links/', include('links.urls')),
    path('inheritance/', include('inheritance.urls')),
    path('form_app/', include('form_app.urls')),
    path('form_app2/', include('form_app2.urls')),
    path('form_app3/', include('form_app3.urls')),
    path('form_app4/', include('form_app4.urls')),
    path('relations/', include('relations.urls')),
]
