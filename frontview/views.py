from django.shortcuts import render

# Create your views here.

def home(request,username):
    return render(request,'frontview/index.html')
