from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list,name='post_list'),
    # 跳转页面
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # 显示图标
    path('post/new/', views.post_new, name='post_new'), 
    # 添加笔写入管理页面
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]



