from django.db import models
from martor.models import MartorField


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

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']