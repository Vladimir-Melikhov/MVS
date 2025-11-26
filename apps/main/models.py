from django.db import models
from django.utils.translation import gettext_lazy as _

class ProjectsModel(models.Model):
    name = models.CharField(_("name"), max_length=30)
    slug = models.SlugField(_("slug"), max_length=100, unique=True)
    description = models.CharField(_("description"), max_length=300)
    demonstration = models.BooleanField(_("demonstration"), default=True)
    author = models.CharField(_("author"), max_length=50)
    poster = models.ImageField(_('poster_main'), upload_to='main/posters/', blank=True)
    poster_2 = models.ImageField(_('poster_2'), upload_to='main/posters/', blank=True)
    poster_3 = models.ImageField(_('poster_3'), upload_to='main/posters/', blank=True)
    link = models.URLField(
        _("project link"), 
        max_length=200, 
        blank=True, 
        null=True
    )

    def __str__(self):
        return self.name
