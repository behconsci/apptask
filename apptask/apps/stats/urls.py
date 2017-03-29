from django.conf.urls import url

from apptask.apps.stats.views import detail, index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<pk>\d+)/$', detail, name='detail'),
]
