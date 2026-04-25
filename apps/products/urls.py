from django.urls import path
from .views import *


urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('products/', ProductListView.as_view(), name='products'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]


