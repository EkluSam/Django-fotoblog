from django.contrib import admin
from authentication.models import User
from .models import Blog, Photo

# Register your models here.
admin.site.register(Blog)
admin.site.register(Photo)
admin.site.register(User)