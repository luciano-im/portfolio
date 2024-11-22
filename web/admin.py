from django.contrib import admin
from django.utils.translation import gettext as _

from web.forms import PostForm
from web.models import Post


class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ('title', 'created_at', 'published_at', 'status', 'post_type')
    list_filter = ('status', 'published_at', 'post_type')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': (('title', 'slug'), 'post_type', 'status', 'published_at', 'tags',),
        }),
        (_('Contenido'), {
            'fields': ('content',),
        }),
        (_('Extracto'), {
            'fields': ('excerpt',),
        }),
    )


admin.site.register(Post, PostAdmin)