# Django Utils
from django.shortcuts import render, redirect

# Import Models
from lists.models import Item, List

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

# View List
def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

# Creates a New list
def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the-only-list-in-the-world/')

