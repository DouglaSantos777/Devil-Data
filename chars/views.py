from django.shortcuts import render
from django.http import HttpResponse

def chars_list(request):
    return render(request, "chars_list.html")