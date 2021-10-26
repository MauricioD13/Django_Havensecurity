from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def haven(request):
    return render(request, 'haven/haven0.html')


def details(request):
    return render(request, 'haven/HavenSecurity_Doc.html')

def about(request):
    return render(request, 'haven/about.html')

