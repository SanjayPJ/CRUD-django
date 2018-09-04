from django.shortcuts import render, redirect, get_object_or_404
from .models import Demo
from .forms import DemoForm

# Create your views here.

def index(request):
    return render(request, "index.html")

def read(request):
    objs = Demo.objects.all()
    return render(request, "view_controller/read.html", {
        "objs" : objs,
    })

def create(request):
    if request.method == "POST":
        form = DemoForm(request.POST)
        if form.is_valid():
            form.save()
    form = DemoForm()
    return render(request, "view_controller/create.html", {
        "form" : form,
    })

def update(request, pk):
    post = get_object_or_404(Demo, pk=pk)
    form = DemoForm(instance=post)
    if request.method == 'POST':
        form = DemoForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, "view_controller/update.html", {
        "form" : form,
    })

def delete(request, pk):
    Demo.objects.filter(pk=pk).delete()
    return redirect('index')