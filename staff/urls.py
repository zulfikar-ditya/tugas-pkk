from django.urls import path

from . import views

app_name = 'staff'

urlpatterns = [
    path('', views.index, name='index'),
    path('power-used/add/', views.add_uses_id, name='add_uses_id'),
    path('power-used/add/<str:username>/', views.addUses, name='addUses'),
    path('power-used/list/', views.powerUsedList, name='powerUsedList'),
    path('power-used/edit/<int:id>/', views.editPowerUsed, name="editPowerUsed"),

    path('bill/list/', views.autoAddBill, name='list_bill'),
    
    path('payment/confirm/<int:id>/', views.paymentConfirm, name='paymentConfirm'),
    path('payment/list', views.paymentlist, name='paymentlist'),
]
