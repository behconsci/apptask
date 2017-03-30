from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from apptask.apps.stats.models import Site


class TestStats(TestCase):
    def setUp(self):
        self.site = Site.objects.create(name='test site')
        self.stat1 = self.site.site_stats.create(
            a_value=2.2, b_value=3.3
        )
        self.stat2 = self.site.site_stats.create(
            a_value=3.2, b_value=4.3
        )

    def test_index(self):
        client = Client()
        page = client.get(reverse('index'))
        # test index page rendering
        self.assertEqual(page.status_code, 200)

        # test if content is rendered correctly
        self.assertIn('Test Site', page.content)

    def test_detail(self):
        client = Client()
        detail_page = client.get(reverse('detail', kwargs={'pk': self.site.id}))

        # test page status
        self.assertEqual(detail_page.status_code, 200)

        # test if content rendered correctly
        self.assertIn('Test Site', detail_page.content)

    def test_summary(self):
        client = Client()
        summary_page = client.get(reverse('summary'))

        # test page status
        self.assertEqual(summary_page.status_code, 200)

        # test if summary SUM rendered correctly
        sites = summary_page.context[0].get('sites')
        for site in sites:
            self.assertEqual(site.sum_a, 5.4)
            self.assertEqual(site.sum_b, 7.6)

        summary_avg_page = client.get(reverse('summary_average'))

        # test page status
        self.assertEqual(summary_avg_page.status_code, 200)

        # test if summary AVG rendered correctly
        sites = summary_avg_page.context[0].get('sites')
        for site in sites:
            self.assertEqual(site.avg_a, 2.7)
            self.assertEqual(site.avg_b, 3.8)
