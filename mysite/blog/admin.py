from django.contrib import admin

# Register your models here.

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created_on', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'created_on'
    ordering = ['status', 'created_on']

admin.site.register(Post, PostAdmin)