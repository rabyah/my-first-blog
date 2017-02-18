from django.contrib import admin
from .models import Post

#makes model (Post from models.py) visible on admin page
admin.site.register(Post)