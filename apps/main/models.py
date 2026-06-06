from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import URLValidator
from django.utils.text import slugify


class ProjectsModel(models.Model):
    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField(_('slug'), max_length=150, unique=True, db_index=True)
    description = models.TextField(_('description'), max_length=500)
    demonstration = models.BooleanField(_('demonstration'), default=True)
    author = models.CharField(_('author'), max_length=100)

    poster = models.ImageField(
        _('poster_main'),
        upload_to='projects/posters/%Y/%m/',
        blank=True, 
        null=True
    )
    poster_2 = models.ImageField(
        _('poster_2'), 
        upload_to='projects/posters/%Y/%m/', 
        blank=True, 
        null=True
    )
    poster_3 = models.ImageField(
        _('poster_3'), 
        upload_to='projects/posters/%Y/%m/', 
        blank=True, 
        null=True
    )
    
    link = models.URLField(
        _('project link'), 
        max_length=300,
        blank=True, 
        null=True,
        validators=[URLValidator()]
    )

    is_active = models.BooleanField(_('active'), default=True, db_index=True)
    order = models.IntegerField(_('order'), default=0, db_index=True)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')
        ordering = ['order', '-created_at']
        indexes = [
            models.Index(fields=['is_active', 'order']),
            models.Index(fields=['-created_at']),
        ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
