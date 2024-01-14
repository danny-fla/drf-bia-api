from django.urls import path
from quicksnap import views

urlpatterns = [
    path('quicksnap/', views.QuicksnapList.as_view()),
]