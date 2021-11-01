from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Widget
from .forms import WidgetForm

def index(request):
    widgets = Widget.objects.all()
    forms = WidgetForm()
    return render(request, 'index.html', {'widgets': widgets, 'forms': forms })

def delete(request, id):
    Widget.objects.get(id=id).delete()
    return redirect('/')

def create_widget(request):
    form = WidgetForm(request.POST)
    print(request.POST)
    if form.is_valid():
        new_widget = form.save(commit=False)
        new_widget.save()
    return redirect('index')