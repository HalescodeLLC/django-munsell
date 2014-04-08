from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest

from .views import home_page
from .models import MunsellColor


# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('mcolor/home.html')
        self.assertEqual(response.content.decode(), expected_html)

    # def test_home_page_can_save_a_POST_request(self):
    #     request = HttpRequest()
    #     request.method = 'POST'
    #     request.POST['munsell_color'] = '5YR 4/6'

    #     response = home_page(request)

    #     self.assertIn('5YR 4/6', response.content.decode())
    #     expected_html = render_to_string('mcolor/home.html',
    #         {'rgb_value': '


class MunsellColorModelTest(TestCase):

    fixtures = ['data.json']

    def setUp(self):
        #  fixture pk=1
        self.color01 = MunsellColor()
        self.color01.hue_a = '0'
        self.color01.hue_b = 'N'
        self.color01.value = '2.5'
        self.color01.chroma = ''
        self.color01.nice_name = 'Black'
        self.color01.munsell_name = 'N 2.5/'
        self.color01.sortable_name = '00N 2.5/'
        self.color01.n_r = '0.2353'
        self.color01.n_g = '0.2353'
        self.color01.n_b = '0.2353'
        self.color01.s_r = '60'
        self.color01.s_g = '60'
        self.color01.s_b = '60'
        self.color01.hexval = '3C3C3C'
        self.color01.save()
        #  fixture pk=42
        self.color02 = MunsellColor()
        self.color02.hue_a = '2.5'
        self.color02.hue_b = 'Y'
        self.color02.value = '8'
        self.color02.chroma = '6'
        self.color02.nice_name = 'Yellow'
        self.color02.munsell_name = '2.5Y 8/6'
        self.color02.sortable_name = '02.5 8/6'
        self.color02.n_r = '0.898'
        self.color02.n_g = '0.7686'
        self.color02.n_b = '0.4824'
        self.color02.s_r = '229'
        self.color02.s_g = '196'
        self.color02.s_b = '123'
        self.color02.hexval = 'E5C47B'
        self.color02.save()

    def test_fixture_loaded_properly(self):
        record = MunsellColor.objects.get(pk=1)
        self.assertEqual(record.munsell_name, self.color01.munsell_name)

    def test_returns_normalized_RGB_components(self):
        x = MunsellColor.objects.get(pk=42).convert_to_normalized_rgb()
        self.assertEqual('0.898', x[0])
        self.assertEqual('0.7686', x[1])
        self.assertEqual('0.4824', x[2])

    def test_returns_standard_RGB_components(self):
        x = MunsellColor.objects.get(pk=42).convert_to_standard_rgb()
        self.assertEqual('229', x[0])
        self.assertEqual('196', x[1])
        self.assertEqual('123', x[2])
