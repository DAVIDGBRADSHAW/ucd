from django.shortcuts import render

def home(request):
    return render(request, "ablog/home.html")