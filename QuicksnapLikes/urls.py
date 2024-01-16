from django.urls import path
from QuicksnapLikes import views

urlpatterns = [
    path('quicksnaplikes/', views.QuicksnapLikeList.as_view(), name='quicksnap-like-list'),
    path('quicksnaplikes/<int:pk>/', views.QuicksnapLikeDetail.as_view(), name='quicksnap-like-detail'),
]