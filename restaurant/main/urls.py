from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('order-table/', views.order_table, name='order_table'),
    path('order/', views.order, name='order'),
    path('order_success/<str:success>/', views.order_success, name='order_success'),
]