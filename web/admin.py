from django.contrib import admin
from django.utils.translation import gettext as _

from web.forms import PostForm, ProjectForm
from web.models import Post, Project, ProjectImage
from web.models import TagPost, TagProject


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ('title', 'created_at', 'published_at', 'status', 'post_type')
    list_filter = ('status', 'published_at', 'post_type')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': (('title', 'slug'), 'post_type', 'status', 'published_at', 'tags'),
        }),
        (_('Contenido'), {
            'fields': ('content',),
        }),
        (_('Extracto'), {
            'fields': ('excerpt',),
        }),
    )


class ProjectImageInline(admin.StackedInline):
    model = ProjectImage
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    list_display = ('name', 'year', 'overview', 'active')
    list_filter = ('active', 'name', 'year')
    inlines = [ProjectImageInline]
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (None, {
            'fields': (('name', 'slug'), 'active', 'year', 'tech', 'featured_image'),
        }),
        (_('URLs'), {
            'fields': ('repo', 'url',),
        }),
        (_('Resumen'), {
            'fields': ('overview',),
        }),
        (_('Contenido'), {
            'fields': ('intro', 'goals', 'challenges', 'solutions', 'impact', 'conclusion',),
        }),
    )


admin.site.register(TagPost, TagAdmin)
admin.site.register(TagProject, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Project, ProjectAdmin)