from django.contrib import admin

from .models import Site, SiteStats


class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_stats')

    def number_of_stats(self, obj):
        return obj.site_stats.count()
    number_of_stats.short_description = 'Number of Stats'


class SiteStatsAdmin(admin.ModelAdmin):
    list_display = ('site', 'a_value', 'b_value', 'date')

admin.site.register(Site, SiteAdmin)
admin.site.register(SiteStats, SiteStatsAdmin)
