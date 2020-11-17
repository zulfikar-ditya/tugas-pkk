from django.urls import path

from . import views

app_name = 'staff'

urlpatterns = [
    path('', views.index, name='index'),
    path('power-used/add/', views.add_uses_id, name='add_uses_id'),
    path('power-used/add/<str:username>/', views.addUses, name='addUses'),
    path('power-used/list/', views.powerUsedList, name='powerUsedList'),
]
