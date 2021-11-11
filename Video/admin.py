from django.contrib import admin

# Register your models here.
from Video.models import Category, Video, Author

admin.site.register(Category)
admin.site.register(Video)
admin.site.register(Author)