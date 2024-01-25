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
    # 新建为草稿里面存放的url
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    # 发布按钮显示页面
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    # 在点击草稿箱后再编辑帖子的界面删除按钮，点击后删除帖子
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    # 访客添加评论
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    # （点赞和不想要的）两个评论功能
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]



