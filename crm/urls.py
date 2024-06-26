from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-product/', views.add_product, name='add-product'),
    path('<str:category>/', views.view_products, name='view-products'),
]