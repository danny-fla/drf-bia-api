from django.urls import path
from RecipeLike import views

urlpatterns = [
    path('recipelike/', views.RecipeLikeList.as_view(), name='recipe-like-list'),
    path('RecipeLike/<int:pk>/', views.RecipeLikeDetail.as_view(), name='recipe-like-detail'),
]