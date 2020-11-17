from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='home'),
    path('my-bill/', views.myBill, name='myBill'),
    path('register/', views.register, name='register'),
]
