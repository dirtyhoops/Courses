from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index(request):
    courses = Course.objects.all()
    context = {
        "courses": courses
    }
    return render(request, "first_app/index.html", context)

def new(request):
    if request.method == 'POST':
        errors = Course.objects.basic_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
        else:
            name = request.POST['name']
            desc = request.POST['description']
            Description.objects.create(description = desc, course = Course.objects.create(name = name))
    return redirect('/')

def delete(request, id):
    course = Course.objects.get(id = id)
    course.delete()
    return redirect('/')