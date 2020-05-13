# Django 社团管理项目开发

## 开发功能说明

社团管理项目主要需要实现以下功能：

1. 普通用户：注册、报名参加社团（或退出社团）、系统登陆、参加活动、查看活动。 

2. 系统管理员: 社团创建和管理、设置社长。 

3. 社长：确认社团成员、发布活动、查看活动报名人员、确认报名人员。 
4. 活动需包括时间、地点、活动内容、建议参加人员、组织者等，还需要有包括开始时间、截至时间。



## 项目部署

```shell
git clone https://github.com/AbyssLink/django_club.git

cd django_club

# install dependencies
pip install django pillow django-crispy-forms

# run server, then access 127.0.0.1:8000
python manage.py runserver
```

注：该项目在 Python 3.7.7 下开发。已知在 Python 3.7 下运行会失败，无法访问 Admin page，暂未找到具体原因。



## 项目简介

本项目基于 Django。Django是一个开放源代码的Web应用框架，由Python写成。采用了MVT的软件设计模式，即模型（Model），视图（View）和模板（Template）。它在开发初期用于管理劳伦斯出版集团旗下的一些以新闻为主的网站。Django的主要目标是简化数据库驱动的网站的开发。Django注重组件的重用性和“可插拔性”，敏捷开发和DRY法则（Don't Repeat Yourself）。在Django中普遍使用的语言是Python，甚至包括配置文件和数据模型。

本项目的开发参考视频教程：https://youtu.be/UmljXZIypDc

本项目源码：https://github.com/AbyssLink/django_club

### 技术栈

后端：Python3.7.7，Django

数据库：SQLite3

前端样式：BootStarp4 CSS

前端模版：Django Temaplates

辅助工具：crispy_forms_tags（表单模版），Pillow（图片处理）

### ScreenShots

| Admin 界面                                                   | Home  页面                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![Xnip2020-05-08_16-18-26](https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/05-08-2020_191935.jpg) | ![Xnip2020-05-08_16-18-53](https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/05-08-2020_191938.jpg) |
| Post 详细页面                                                | Register 页面                                                |
| ![Xnip2020-05-08_16-44-04](https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/05-08-2020_191940.jpg) | ![Xnip2020-05-08_16-45-07](https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/05-08-2020_191942.jpg) |
| User 列表                                                    | User Profile 页面                                            |
| ![Xnip2020-05-08_16-18-58](https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/05-08-2020_191943.jpg) | ![Xnip2020-05-08_16-19-06](https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/05-08-2020_191945.jpg) |
| 某 User 参加的活动列表页面                                   | 某活动报名的 User 列表页面                                   |
| ![Xnip2020-05-08_16-44-20](https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/05-08-2020_191946.jpg) | ![Xnip2020-05-08_16-44-49](https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/05-08-2020_191948.jpg) |
| Club 列表                                                    | Club 下的社员                                                |
| ![Xnip2020-05-13_12-08-56](/Users/chiya/Pictures/picto_compress/Xnip2020-05-13_12-08-56.jpg) | ![Xnip2020-05-13_12-10-06](/Users/chiya/Pictures/picto_compress/Xnip2020-05-13_12-10-06.jpg) |



## 项目实现

### 项目文件结构

```shell
.
├── club	# club 模块
│   ├── __init__.py
│   ├── admin.py		# 模块注册
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py		# migrations 操作描述
│   │   ├── 0002_auto_20200507_1737.py
│   │   ├── __init__.py
│   ├── models.py		# model 定义
│   ├── static			# 静态文件，HTML/CSS/JS 等
│   │   └── club
│   │       └── main.css		# 主 CSS
│   ├── templates						# club 模版
│   │   └── club
│   │       ├── about.html		# 关于页面
│   │				├── attend_by_user.html		# 当前用户参加的社团列表页
│   │       ├── attend_create.html		# 用户参加社团后返回页
│   │       ├── attend_home.html			# 当前社团参加的用户列表页
│   │       ├── base.html			# 基础页面（页面框架）
│   │       ├── club_detail.html			# 社团详情页
│   │       ├── club_home.html				# 社团列表页
│   │       ├── home.html			# 主页（现实活动列表）
│   │       ├── join_by_user.html		# 当前用户参加的活动列表页
│   │       ├── join_create.html		# 用户参加活动后返回页
│   │       ├── join_home.html			# 当前活动参与的用户列表页
│   │       ├── post_confirm_delete.html		# 确认删除页
│   │       ├── post_detail.html		# 活动详情页
│   │       ├── post_form.html			# 活动表单
│   │       ├── user_posts.html			# 当前用户发布的活动列表页
│   │       └── users.html					# 用户列表页面（仅查看）
│   ├── tests.py
│   ├── urls.py			# club 模块下 url 映射定义
│   └── views.py		# club 模块下 views 定义
├── db.sqlite3		# SQLite3 数据库文件
├── debug.log			# Logger debug 文件
├── django_project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py		# 全局 Settings 设置
│   ├── urls.py			# 全局 URL 映射
│   └── wsgi.py
├── manage.py
├── media				# 媒体文件（不使用 Git 记录）
│   ├── default.jpg
│   └── profile_pics
│       └── the_abysswalker_by_shimhaq98_dbubuu6-fullview.jpg
└── users		# users 模块
    ├── __init__.py
    ├── admin.py		# 模块注册
    ├── apps.py
    ├── forms.py  	# 自定义表单
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── 0002_profile_role.py
    │   ├── __init__.py
    ├── models.py		# model 定义
    ├── signals.py
    ├── templates		# users 模块模版
    │   └── users
    │       ├── login.html			# 用户登录页
    │       ├── logout.html			# 用户登出页
    │       ├── profile.html		# 用户概述页
    │       └── register.html		# 注册新用户页
    ├── tests.py
    └── views.py							# user 模块下 views 定义
```





### Model 设计

#### ER 图 

Django 自带了许多的辅助类，看上去有些杂乱..只截图了自建的实体和关系

![Xnip2020-05-13_12-04-41](/Users/chiya/Pictures/picto_compress/Xnip2020-05-13_12-04-41.jpg)



### 基础工程

创建 start-project:

```shell
 django-admin startproject mysite
```

创建 super user

```shell
python3 manage.py createsuperuser
```

运行 server，会进行热更新

```shell
python3 manage.py runserver
```

本项目下共有两个字定义 Python Model 模块：Club （post，join），User（profile）

创建 model，如 Profile model：

```python
class Profile(models.Model):
    # if user is delete, also delete profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # default user role is a normal user, and can only update by super admin
    role = models.PositiveSmallIntegerField(default=ROLES['NORMAL'])

    def __str__(self):
        return f'{self.user.username} Profile'
```

创建数据库模型并执行，以下为 UserProfile 的示例：

```shell
# 1. Make migrations
python manage.py makemigrations
Migrations for 'users':
  users/migrations/0001_initial.py
    - Create model Profile
(admin)

# 2. then Apply migrations
python manage.py migrate       
Operations to perform:
  Apply all migrations: admin, auth, club, contenttypes, sessions, users
Running migrations:
  Applying users.0001_initial... OK
(admin)

# 3. then register model in admin.py
admin.site.register(Profile)
```

也可以使用 Django 的 Shell 进行数据库 CRUD 操作，以下对 model 进行操作的示例：

```shell
# use python prompt 
python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.all()
<QuerySet [<User: Sion>, <User: TestUser>]>
>>> Post.objects.all()
<QuerySet []>
>>> User.objects.first()
<User: Sion>
>>> User.objects.filter(username='Sion')
<QuerySet [<User: Sion>]>
>>> User.objects.filter(username='Sion').first()
<User: Sion>
```



### 超级管理员

超级管理员拥有最高的权限并拥有 Django 提供的 Admin Page。

创建超级管理员：

```shell
 python manage.py createsuperuser
```

登陆进入管理页面，可以快速对数据库的各表进行 CRUD，可快速订制数据条目查询，过滤和搜索条件。

该后台管理功能在项目需求逐渐复杂，模块越来越多时，该后台管理的功能会非常实用。

![Xnip2020-05-08_16-18-26](https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/05-08-2020_191935.jpg)

### 用户登陆/注册/更新

部分表单使用 crispy_forms_tags 实现，自带了输入校验且为 Bootstrap 风格，符合前端界面的样式，如 Register 模块的前端界面设计：

```html
<!- /template/users/register.html -!>
<form method="POST">
  {% csrf_token %}
  <fieldset class="form-group">
    <legend class="border-bottom mb-4">Join Today</legend>
    {{ form|crispy }}
  </fieldset>
  <div class="form-group">
    <button class="btn btn-outline-info" type="submit">Sign Up</button>
  </div>
</form>
```

crispy_forms_tags 的字段可以自行设计：

```python
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# 用户注册表单
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# 用户信息更新表单
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# 用户概述更新表单
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

```

用户上传头像时，使用 Pillow 对图片进行适当压缩减小服务器负担：

```python
# overrite the save method
def save(self, *args, **kwargs):
  # run parent save method
  super().save(*args, **kwargs)

  # resize profile image
  img = Image.open(self.image.path)

  if img.height > 300 or img.width > 300:
    # compress image size as 300 x 300 px.
    output_size = (300, 300)
    img.thumbnail(output_size)
    img.save(self.image.path)
```



### 用户鉴权

设置 USER_ROLE 变量标示用户类型

```python
ROLES = {
    'PRESIDENT': 1,
    'NORMAL': 2
}
```

Role 存储在 Model Profile 中，默认为 'NORMAL' （普通学生）

```python
class Profile(models.Model):
    # if user is delete, also delete profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # default user role is a normal user, and can only update by super admin
    role = models.PositiveSmallIntegerField(default=ROLES['NORMAL'])

    def __str__(self):
        return f'{self.user.username} Profile'
```

若需要更改用户权限为 'PRESIDENT' （社长），需要由超级管理员（superuser）在 Django 提供的 admin 管理页中修改。

在 views.py 中鉴权，如：添加 Post 的页面，若用户角色为 Student，则没有创建 Post 的权限，系统会返回 403 Forbidden。

```python
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'location', 'date_start', 'date_end']

    # set author to current user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # check user permission
    def dispatch(self, request, *args, **kwargs):
        # check user role
        if not request.user.profile.role is 1:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
```

在 Update Post 时，需要鉴别用户是否登陆，以及该 Post 是否由该 User 创建：

```python
# club/views.py

# 对 Class Based View，添加 LoginRequiredMixin 等类似的 auth 方法
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'location', 'date_start', 'date_end']

    # set author to current user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # check if this post is wirten by this user
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
```

```python
# 对 Function Based View，添加 login_required 装饰器
@login_required
def profile(request):
    if request.method == 'POST':
        # give instance value to process user data
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # give success message to let user known
            messages.success(
                request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context=context)
```

通过鉴权操作，可以在后端实现验证用户请求是否符合权限。

同时，在前端为不同 ROLE 的 user 渲染不同的页面，如 Base 页面中，为 superadmin，President，Student 渲染不同的组件。

```python
<p class='text-muted'>
	<ul class="list-group">
		{% if user.is_staff %}
			<li class="list-group-item list-group-item-light">
				<a href="/admin">Admin Page</a>
			</li>
		{% endif %}
		{% if user.profile.role is 1 %}
			<li class="list-group-item list-group-item-light">
				<a href="{% url 'profile' %}">Profile (Prisdent)</a>
			</li>
		{% endif %}
		{% if user.profile.role is 2 %}
			<li class="list-group-item list-group-item-light">
				<a href="{% url 'profile' %}">Profile (Student)</a>
			</li>
		{% endif %}
		{% if user.profile.role is 1 or user.is_staff %}
			<li class="list-group-item list-group-item-light">
				<a href="{% url 'club-users' %}">See Users</a>
			</li>
		{% endif %}
			<li class="list-group-item list-group-item-light">
				<a href="{% url 'join-by-user' %}">My Joined Activity</a>
			</li>
			<li class="list-group-item list-group-item-light">Announcements</li>
			<li class="list-group-item list-group-item-light">Calendars</li>
	</ul>
</p>
```



### 活动创建/更新/报名

Model 定义

```python
# 活动 Model 定义，Author 字段为外键，CASCADE 常量代表外键删除后该数据也会删除
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    location = models.CharField(
        default='ZUCC Univercity Library', max_length=100)
    date_start = models.DateTimeField(default=timezone.now)
    date_end = models.DateTimeField(default=timezone.now)
    date_posted = models.DateTimeField(default=timezone.now)
    # if the user is deleted, delete the post as well
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # use it as redirect
    # reverse will return the full path as a string
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
      
# 参加(Relationship) Model 定义，user 和 post 字段为外键
class Join(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} -> {self.post.title}'
```

用户参加某个活动

```python
@login_required
def joinCreate(request, pk):
    context = {}
    join = Join()
    post = get_object_or_404(Post, pk=pk)
    # 判断用户是否已报名该活动
    count = len(Join.objects.filter(user=request.user, post=post))
    if count is 0:
        is_joined = False
        join.user = request.user
        join.post = post
       	# commit to database 
        join.save()
    else:
        is_joined = True

    context = {
        'post_title': post.title,
        'username': request.user.username,
        'is_joined': is_joined
    }

    return render(request, 'club/join_create.html', context)
```



### 分页实现

Django 的 Class Based View 中自带了分页的设置，分页可以帮助我们按需获取资源，加快加载速度并减小服务器压力。以活动列表页面为例：

```python
class PostListView(ListView):
    model = Post
    template_name = 'club/home.html'
    context_object_name = 'posts'
    # inverse order as date_posted
    ordering = ['-date_posted']
    paginate_by = 5
```

前端模版中实现分页：

```html
{% if is_paginated %}
  {% if page_obj.has_previous %}
    <a class='btn btn-outline-info mb-4' href='?page=1'>First</a>
    <a class='btn btn-outline-info mb-4' href='?page={{ page_obj.previous_page_number }}'><</a>
  {% endif %}

  {% for num in page_obj.paginator.page_range %}
    {% if page_obj.number == num %}
      <a class='btn btn-info mb-4' href='?page={{ num }}'>{{ num }}</a>
    {% elif num > page_obj.number|add:'-3' and  num < page_obj.number|add:'3' %}
      <a class='btn btn-outline-info mb-4' href='?page={{ num }}'>{{ num }}</a>
    {% endif %}
  {% endfor %}

  {% if page_obj.has_next %}
    <a class='btn btn-outline-info mb-4' href='?page={{ page_obj.next_page_number }}'>></a>
    <a class='btn btn-outline-info mb-4' href='?page={{ page_obj.paginator.num_pages }}'>Last</a>
  {% endif %}
{% endif %}
{% endblock content %}
```

效果

![Xnip2020-05-08_16-18-58](https://raw.githubusercontent.com/AbyssLink/pic/master/uPic/05-08-2020_191943.jpg)



### Debug 功能实现

Django 默认自带了许多 Debug 工具，我选用了 Logger，配置如下：

```python
# settings.py
# Logger settings
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```

需要使用 Logger 的需要在对应的上文中获取 logger 实例：

```python
# Get an instance of a logger
logger = logging.getLogger('django')

# debug
logger.debug(f'count === {count}')

# see it at debug.log file
```

