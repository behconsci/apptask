from django.shortcuts import render
from django.db.models import Sum

from apptask.apps.stats.models import Site


def index(request):
    sites = Site.objects.all()
    return render(request, 'index.html', {
        'sites': sites
    })


def detail(request, pk):
    site = Site.objects.get(pk=pk)
    return render(request, 'detail.html', {
        'site': site
    })


def summary(request):
    """ with django orm """
    sites = Site.objects.annotate(sum_a=Sum('site_stats__a_value'), sum_b=Sum('site_stats__b_value'))
    return render(request, 'summary.html', {
        'sites': sites
    })


def summary_average(request):
    """ with raw sql """
    raw_sql = 'SELECT "stats_site"."id", "stats_site"."name", ' \
              'AVG("stats_sitestats"."a_value") AS "avg_a", ' \
              'AVG("stats_sitestats"."b_value") AS "avg_b" ' \
              'FROM "stats_site" LEFT OUTER JOIN "stats_sitestats" ON ' \
              '("stats_site"."id" = "stats_sitestats"."site_id") ' \
              'GROUP BY "stats_site"."id", "stats_site"."name"'

    sites = Site.objects.raw(raw_sql)
    return render(request, 'summary.html', {
        'sites': sites
    })
