from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
 list_display = ['name', 'author', 'posted', 'status']
 list_filter = ['status', 'created', 'posted', 'author']
 search_fields = ['name', 'description']
 prepopulated_fields = {'slug': ('name',)}
 raw_id_fields = ['author']
 date_hierarchy = 'posted'
 ordering = ['status', 'posted']
 show_facets = admin.ShowFacets.ALWAYS