from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view()),
    path('categories/<int:pk>/', CategoryDetailView.as_view()),
    path('foods/', FoodListCreateView.as_view()),
    path('foods/<int:pk>/', FoodDetailView.as_view()),
    path('orders/', OrderListCreateView.as_view()),
    path('orders/<int:pk>/', OrderDetailView.as_view()),
]
