from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def show_view(request):
    return HttpResponse( "<p> Mnha view do app Títulos </p>")

def show_template(request):
    return HttpResponse( "<p> Minha view do app Títulos usando template </p>")
