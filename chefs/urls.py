from django.urls import path
from chefs import views

urlpatterns = [
    path('chefs/', views.ChefList.as_view()),
    path('chefs/<int:pk>/', views.ChefDetail.as_view())
]
