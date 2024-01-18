from django.urls import path
from RecipeComments import views

urlpatterns = [
    path('recipecomments/', views.RecipeCommentList.as_view()),
    path('recipecomments/<int:pk>/', views.RecipeCommentDetail.as_view())
]