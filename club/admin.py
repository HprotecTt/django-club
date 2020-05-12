from django.contrib import admin

from .models import Attend, Club, Join, Post

# Register your models here.
admin.site.register(Post)
admin.site.register(Join)
admin.site.register(Club)
admin.site.register(Attend)
