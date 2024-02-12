from django.urls import path
from recipe import views

urlpatterns = [
    path('recipe/', views.RecipeList.as_view()),
    path('recipe/<int:pk>/', views.RecipeDetail.as_view())
]
