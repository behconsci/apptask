from __future__ import unicode_literals

from django.db import models
from django.utils.functional import cached_property
from django.core.urlresolvers import reverse


class Site(models.Model):
    name = models.CharField(max_length=100)

    @cached_property
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})

    def __unicode__(self):
        return self.name


class SiteStats(models.Model):
    site = models.ForeignKey(Site, related_name='site_stats')
    date = models.DateTimeField(auto_now_add=True)
    a_value = models.FloatField(default=0.0)
    b_value = models.FloatField(default=0.0)
