from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
# 跳转到新增的页面
from django.shortcuts import redirect
# 授权添加/编辑帖子
from django.contrib.auth.decorators import login_required
# 导入评论模块
from .forms import PostForm, CommentForm
# 导入模块里面的帖子和评论模块
from .models import Post, Comment

# 添加我们的视图
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# 添加我们的视图
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
# 转到新增的视图
def post_new(request):
    if request.method == 'POST':
        form= PostForm(request.POST)
        # 判断是否有效，并保存
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # 下行注释掉就表明了新建为草稿存储  不在是保存并发布了
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form}) 

@login_required
# 视图
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # 下行注释掉就表明了新建为草稿存储  不在是保存并发布了
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
# 我们新建的草稿存储并显示出来
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
# 发布后的最后一个视图
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

# 显示发布帖子后再回到界面显示有帖子
def publish(self):
    self.published_date = timezone.now()
    self.save()

@login_required
# 在草稿箱里面编辑帖子，除了有发布和编辑、再就是删除功能
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

@login_required
# 访客添加评论
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
# 用户授权的评论
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
# 用户未授权的评论
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)