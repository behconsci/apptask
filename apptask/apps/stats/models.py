from __future__ import unicode_literals

from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=100)
    a_value = models.FloatField(default=0.0)
    b_value = models.FloatField(default=0.0)

    def __unicode__(self):
        return self.name
