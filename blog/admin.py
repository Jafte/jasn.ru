from django.contrib import admin
from blog.models import Blog, Post, PostImage
from guardian.admin import GuardedModelAdmin

admin.site.register(Blog, GuardedModelAdmin)
admin.site.register(Post, GuardedModelAdmin)
admin.site.register(PostImage, GuardedModelAdmin)
