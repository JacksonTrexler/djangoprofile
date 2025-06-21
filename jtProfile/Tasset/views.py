from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<html style=\"color:red;\">Get ready for Tasset!</html>")