from django.http import request
from django.http.request import HttpRequest
from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'home.html', {'new_list_item': request.POST.get('item_text', '')})