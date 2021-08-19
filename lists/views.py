# Django Utils
from django.shortcuts import render, redirect

# Import Models
from lists.models import Item

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

# View List
def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

# Creates a New list
def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')

