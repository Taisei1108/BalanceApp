from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListBalance.as_view()), #とりあえず一覧表示したい
    #path('<int:pk>/', views.DetailDaily.as_view()), #1日の詳細
    #path('<str:cat>/', views.CategoryDairy.as_view()), #カテゴリ別一覧
]
