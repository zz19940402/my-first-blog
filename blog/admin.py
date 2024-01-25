from django.contrib import admin
from .models import Post,Comment

# 添加帖子模型
admin.site.register(Post)

# 添加评论模型
admin.site.register(Comment)
