<!-- --w10安装虚拟环境在djangogirls文件下
python -m venv myvenv
--windows运行虚拟环境
myvenv\Scripts\activate
--linux进入虚拟环境
source myvenv/bin/activate
--准备安装Django；升级pip
python -m pip install --upgrade pip
--创建requirements.txt
Django~=3.2.10
--安装Django
pip install -r requirements.txt
--在myvenv下运行django创建目录（注意点）
django-admin.exe startproject mysite .
--mysite/settings.py更改设置
TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'de-ch'
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']
--博客创建数据库
python manage.py migrate
--启动 Web 服务器
python manage.py runserver


--创建应用
python manage.py startapp blog
--mysite/settings.py更改设置
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]
--创建博客文章模型
【很多。。。】
--为数据库中的模型创建表
python manage.py makemigrations blog
--Django 管理员：blog/admin.py更新
from django.contrib import admin
from .models import Post
admin.site.register(Post)
--重启服务
python manage.py runserver
--登录管理页面
http://127.0.0.1:8000/admin/
--创建超级用户
python manage.py createsuperuser
--内容如下
user:zzone7777
E-mail:951054670@qq.com
passwd:123456
--登录后台管理，添加数据

--部署第三方平台-PythonAnywhere---github
<!-- --git下载准备
--创建文件.gitignore添加以下【东西很多。。。】
--初始化按步骤操作。。。git status---git add .---git commit -m "My Django Girls app, first commit"
--git remote add origin https://github.com/zz19940402/my-first-blog.git---git push -u origin HEAD
---注册https://www.pythonanywhere.com/免费账户
user:zzone7777
passwd:ZZ15282210497
--API记住重要
d70180dc0e0fa5dd77a1090ef9e3a336001f6970
--调用实例
import requests
username = 'zzone7777'
token = 'd70180dc0e0fa5dd77a1090ef9e3a336001f6970'

response = requests.get(
    'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
        username=username
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
    print('CPU quota info:')
    print(response.content)
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))
--Bash 控制台31963943安装 PythonAnywhere
pip3.8 install --user pythonanywhere
--Bash 控制台31963943安装
pa_autoconfigure_django.py --python=3.8 https://github.com/zz19940402/my-first-blog.git
--启动virtualenv虚拟环境
python manage.py createsuperuser
--添加管理员的信息
user:zzone7777
E-mail:951054670@qq.com
passwd:123456
--在pythonanywhere里面的后台管理中心web配置页面的url地址后面加上/admin/即可访问管理人员后台进行添加删除操作
zzone7777.pythonanywhere.com/admin/


<!--提交代码到github在vsc里面修改后
git status
git add .
git status 
git commit -m "changed the HTML for the site"
git push
--在zzone7777.pythonanywhere.com下pull 更新下载所有的代码
git pull
--->

<!-- --本地打开Django shell
python manage.py shell
--显示所有帖子对象
Post.objects.all()
--报错，忘记导入它
from blog.models import Post
--现在可以显示查看帖子对象了
。。。
--在数据库中创建post对象
Post.objects.create(author=me, title='Sample title', text='Test')
--我们这里缺少一个成分：.我们需要以作者身份传递一个模型实例
from django.contrib.auth.models import User
--我们之前创建的超级用户！现在让我们获取用户的实例（调整此行以使用您自己的用户名）
me = User.objects.get(username='自己的超级用户名')
--在进行创建帖子
Post.objects.create(author=me, title='Sample title', text='Test')
--显示查看创建的帖子
Post.objects.all()
--添加更多帖子
。。。
--筛选对象--找到自己创建的帖子
Post.objects.filter(author=me)
--查找指定--也许我们想在字段中查看所有包含“标题”一词的帖子
Post.objects.filter(title__contains='title')
--获取所有已发布帖子的列表。为此，我们过滤过去设置的所有帖子
from django.utils import timezone
Post.objects.filter(published_date__lte=timezone.now())
--不幸的是，我们从 Python 控制台添加的帖子尚未发布。但我们可以改变这一点！首先获取我们想要发布的帖子的实例：
post = Post.objects.get(title="Sample title")
--发布它
post.publish()
--现在尝试再次获取已发布帖子的列表（按向上箭头键三次并点击）
Post.objects.filter(published_date__lte=timezone.now())
--对对象进行排序
Post.objects.order_by('created_date')
--我们还可以通过在开头添加以下内容来颠倒顺序
Post.objects.order_by('-created_date')
--通过方法链进行复杂查询
Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
--关闭shell
exit()


--模板中的动态数据
from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})
--我们讨论过包含在不同文件中编写的代码吗？现在是我们必须包含我们编写的模型的时刻
from django.shortcuts import render
from .models import Post
--查询集
Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
--让我们在代码编辑器中打开文件，并将这段代码添加到函数中——但不要忘记先添
from django.utils import timezone
posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
--添加参数
return render(request, 'blog/post_list.html',{'posts': posts})


--显示帖子列表模板：Django 模板中打印变量，我们使用双大括号，里面有变量的名称
{{ posts }}
--但是我们希望这些帖子的显示方式与我们之前在 HTML 简介一章中创建的静态帖子一样。您可以混合使用 HTML 和模板标签
<header>
    <h1><a href="/">Django Girls Blog</a></h1>
</header>

{% for post in posts %}
    <article>
        <time>published: {{ post.published_date }}</time>
        <h2><a href="">{{ post.title }}</a></h2>
        <p>{{ post.text|linebreaksbr }}</p>
    </article>
{% endfor %}


--CSS – 让它变得漂亮！让我们使用 Bootstrap包含 Popper 和我们的 JS
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
--Django 中的静态文件:blog/static/css/blog.css
h1 a, h2 a {
    color: #C25100;
}
--id 指向特定元素
<a href="https://en.wikipedia.org/wiki/Django" class="external_link" id="link_to_wiki_page"> -->
