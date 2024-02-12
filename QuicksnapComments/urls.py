from django.urls import path
from QuicksnapComments import views

urlpatterns = [
    path('quicksnapcomments/', views.QuicksnapCommentList.as_view()),
    path('quicksnapcomments/<int:pk>/', views.QuicksnapCommentDetail.as_view())
]
