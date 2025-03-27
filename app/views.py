from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from pprint import pprint


def home(request):
    context = {
        'title': 'Welcome to My Django Site',
        'content': 'This is the home page content. 👻',
    }
    return render(request, 'pages/home.html', context)


def about(request):
    context = {
        'title': 'Welcome to About Page',
        'content': 'This is the about page content. 👻',
    }
    return render(request, 'pages/home.html', context)


def blog(request, id):
    return HttpResponse(f"Viewing blog post #{id}")


def product(request, slug):
    return HttpResponse(f"Product: {slug}")


def custom_404(request, exception):
    return HttpResponse("Oops! Page not found!", status=404)