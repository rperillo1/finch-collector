from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def finches_index(request):
    return render(request, 'finches/index.html')