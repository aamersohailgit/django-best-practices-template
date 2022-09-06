from django.shortcuts import render
from django.http import HttpResponse


def message(request):
    return HttpResponse("Hello App 1")
