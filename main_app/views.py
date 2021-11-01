from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Item
from .forms import ItemForm

def index(request):
    items = Item.objects.all()
    forms = ItemForm()
    return render(request, 'index.html', {'items': items, 'forms': forms })

def delete(request, id):
    Item.objects.get(id=id).delete()
    return redirect('/')

def create_item(request):
    form = ItemForm(request.POST)
    print(request.POST)
    if form.is_valid():
        new_widget = form.save(commit=False)
        new_widget.save()
    return redirect('index')