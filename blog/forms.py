from django import forms

from .models import Post,Comment

# 导入帖子模块
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

# 导入评论模块
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
