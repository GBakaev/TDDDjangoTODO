# Django Utils
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

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
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)
    
    def test_home_page_can_save_POST_request(self):
        request = HttpRequest()
        request.method = "POST"
        request.POST['item_text'] = "A new List Item"

        response = home_page(request)
        self.assertIn("A new List Item", response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'new_item_text':  'A new list item'}
        )
        self.assertEqual(response.content.decode(), expected_html)