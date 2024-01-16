from django.urls import path
from likes import views

urlpatterns = [
    path('likes/', views.LikeList.as_view(), name='like-list'),
    path('likes/<int:pk>/', views.LikeDetail.as_view(), name='like-detail'),
    # path('likes/recipe/<int:pk>', views.LikeRecipeList.as_view(), name='like-recipe-list'),
    # path('likes/quicksnap/', views.LikeQuicksnapList.as_view(), name='like-quicksnap-list'),
]
