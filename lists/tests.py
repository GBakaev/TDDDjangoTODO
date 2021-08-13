# Django Utils
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest, response

# Import Views
from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.view_name, 'home')

    def test_home_view_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>Awesome Lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))