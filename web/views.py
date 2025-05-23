import os
import json
import uuid

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render

from martor.utils import LazyEncoder

from web.models import About, Post, Project


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(active=True).prefetch_related('tech')
        context['posts'] = Post.objects.filter(status='published', post_type='blog').order_by('-created_at')[:3]
        context['thoughts'] = Post.objects.filter(status='published', post_type='thought').order_by('-created_at')[:5]
        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.latest('id')
        return context


class BlogView(ListView):
    template_name = 'blog.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(status='published', post_type='blog').order_by('-created_at')


class ThoughtsView(ListView):
    template_name = 'thoughts.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(status='published', post_type='thought').order_by('-created_at')


class PostView(DetailView):
    model = Post
    template_name = 'post.html'
    queryset = Post.objects.filter(status='published', post_type='blog').prefetch_related('tags')


class ThoughtView(DetailView):
    model = Post
    template_name = 'post.html'
    queryset = Post.objects.filter(status='published', post_type='thought').prefetch_related('tags')


class ProjectsView(ListView):
    template_name = 'projects.html'
    model = Project

    def get_queryset(self):
        return Project.objects.filter(active=True).prefetch_related('tech')


class ProjectView(DetailView):
    model = Project
    template_name = 'project.html'

    def get_queryset(self):
        return Project.objects.prefetch_related('tech', 'project_image').filter(active=True)


@login_required
def markdown_uploader(request):
    """
    Makdown image upload for locale storage
    and represent as json to markdown editor.
    """
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if request.method == 'POST' and is_ajax:
        if 'markdown-image-upload' in request.FILES:
            image = request.FILES['markdown-image-upload']
            image_types = [
                'image/png', 'image/jpg',
                'image/jpeg', 'image/pjpeg', 'image/gif'
            ]
            if image.content_type not in image_types:
                data = json.dumps({
                    'status': 405,
                    'error': _('Formato de imágen incorrecto.')
                }, cls=LazyEncoder)
                return HttpResponse(
                    data, content_type='application/json', status=405)

            if image.size > settings.MAX_IMAGE_UPLOAD_SIZE:
                to_MB = settings.MAX_IMAGE_UPLOAD_SIZE / (1024 * 1024)
                data = json.dumps({
                    'status': 405,
                    'error': _('El tamáño máximo de imágen permitido es de %(size)s MB.') % {'size': to_MB}
                }, cls=LazyEncoder)
                return HttpResponse(
                    data, content_type='application/json', status=405)

            img_uuid = "{0}-{1}".format(uuid.uuid4().hex[:10], image.name.replace(' ', '-'))
            tmp_file = os.path.join(settings.MARTOR_UPLOAD_PATH, img_uuid)
            def_path = default_storage.save(tmp_file, ContentFile(image.read()))
            img_url = os.path.join(settings.MEDIA_URL, def_path)

            data = json.dumps({
                'status': 200,
                'link': img_url,
                'name': image.name
            })
            return HttpResponse(data, content_type='application/json')
        return HttpResponse(_('Solicitud inválida!'))
    return HttpResponse(_('Solicitud inválida!'))