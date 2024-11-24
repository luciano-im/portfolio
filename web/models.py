from django.db import models
from django.utils.translation import gettext_lazy as _
from martor.models import MartorField
from taggit.managers import TaggableManager
from tinymce.models import HTMLField


class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    POST_TYPE_CHOICES = [
        ('blog', 'Blog'),
        ('thought', 'Thought'),
    ]

    title = models.CharField(max_length=200, verbose_name='Título')
    slug = models.SlugField(max_length=200, unique=True)
    content = MartorField(verbose_name='Contenido')
    excerpt = MartorField(verbose_name='Extracto')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')
    published_at = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de Publicación')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name='Estado')
    featured_image = models.ImageField(upload_to='posts/', null=True, blank=True, verbose_name='Imágen Destacada')
    post_type = models.CharField(max_length=10, choices=POST_TYPE_CHOICES, default='blog', verbose_name='Tipo de Post')
    tags = TaggableManager(help_text=_('Selecciona uno o más tags'))

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Nombre del Proyecto'))
    active = models.BooleanField(default=True, verbose_name=_('Activo'))
    overview = HTMLField(verbose_name=_('Descripción General'))
    year = models.DateField(blank=True, null=True, verbose_name=_('Año'))
    repo = models.URLField(null=True, blank=True, verbose_name=_('URL del Repositorio'), help_text=_('URL de GitHub, GitLab, BitBucket, etc.'))
    url = models.URLField(null=True, blank=True, verbose_name=_('URL del Proyecto'))
    intro = HTMLField(verbose_name=_('Introducción'))
    goals = HTMLField(null=True, blank=True, verbose_name=_('Objetivos'))
    challenges = HTMLField(null=True, blank=True, verbose_name=_('Desafíos y Dificultades'))
    solutions = HTMLField(null=True, blank=True, verbose_name=_('Soluciones Implementadas'))
    impact = HTMLField(null=True, blank=True, verbose_name=_('Impactos del Proyecto'))
    conclusion = HTMLField(null=True, blank=True, verbose_name=_('Conclusión'))

    def __str__(self):
        return self.name