from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField
from martor.models import MartorField
from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase
from tinymce.models import HTMLField


class TagPost(TagBase):

    class Meta:
        verbose_name = 'Etiqueta de Post'
        verbose_name_plural = 'Etiquetas de Post'


class TagProject(TagBase):

    class Meta:
        verbose_name = 'Etiqueta de Proyecto'
        verbose_name_plural = 'Etiquetas de Proyecto'


class TaggedPost(GenericTaggedItemBase):
    tag = models.ForeignKey(TagPost, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_items")


class TaggedProject(GenericTaggedItemBase):
    tag = models.ForeignKey(TagProject, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_items")


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
    featured_image = FilerImageField(on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('Imágen Destacada'))
    post_type = models.CharField(max_length=10, choices=POST_TYPE_CHOICES, default='blog', verbose_name='Tipo de Post')
    tags = TaggableManager(through=TaggedPost, help_text=_('Selecciona uno o más tags'))

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Posts')
        verbose_name_plural = _('Post')


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
    tech = TaggableManager(through=TaggedProject, verbose_name=_('Tecnologías'), help_text=_('Selecciona una o más tecnologías'))
    featured_image = FilerImageField(on_delete=models.CASCADE, verbose_name=_('Imágen Destacada'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Proyecto')
        verbose_name_plural = _('Proyectos')


class ProjectImage(models.Model):
    product = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name=_('Proyecto'))
    image = FilerImageField(on_delete=models.CASCADE, verbose_name=_('Imágen'))

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = _('Imágen del Proyecto')
        verbose_name_plural = _('Imágenes del Proyecto')