from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(),name='index'),
    path('boards/', views.BoardsView.as_view(), name='board_games'),
]
