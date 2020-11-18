from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from map.views import map_func

# Create your tests here.


class TestUrls(SimpleTestCase):
    def test_map_url(self):
        url = reverse("map-shelters")
        self.assertEquals(resolve(url).func, map_func)
        self.assertEquals(resolve(url).route, "maps/shelters/")
