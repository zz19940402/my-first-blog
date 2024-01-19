from django.shortcuts import render

# Create your views here.创建一个视图
def post_list(request):
    return render(request, 'blog/post_list.html',{})

