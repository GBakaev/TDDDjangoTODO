# Django Utils
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest, request, response
from django.template.loader import render_to_string
import re

# Import Views
from lists.views import home_page

# Import Models
from lists.models import Item

# Create your tests here.
# Home Page Test
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.view_name, 'home')

    def test_home_view_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)

        # CSRF tokens don't get render_to_string'd
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        observed_html = re.sub(csrf_regex, '', response.content.decode())
        expected_html = render_to_string('home.html')

        self.assertEqual(observed_html, expected_html)

# Item Model Class Test
class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first item'
        first_item.save()

        second_item = Item()
        second_item.text = 'The second item'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertTrue(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first item')
        self.assertEqual(second_saved_item.text, 'The second item')
        
# Url Views
class ListViewTest(TestCase):
    def test_displays_all_items(self):
        Item.objects.create(text='itemey 1') 
        Item.objects.create(text='itemey 2')
        
        response = self.client.get('/lists/the-only-list-in-the-world/')
            
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')

    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')

class NewListTest(TestCase):

    def test_saving_POST_request(self):
        self.client.post(
            '/lists/new',
            data={'item_text': 'A new list item'}
        )
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self): 
        response = self.client.post(
            '/lists/new',
            data={'item_text': 'A new list item'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/lists/the-only-list-in-the-world/')



