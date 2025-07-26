from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('category/<int:pk>/', views.category_products, name='category_products'),
]