from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")

def portfolio(request):
    return render(request, "portfolio.html")

def blog(request):
    return render(request, "blog.html")

def detail(request):
    return render(request, "blog-single.html")

def about(request):
    return render(request, "about.html")

def donate(request):
    return render(request, "donate.html")

def takeaction(request):
    return render(request, "takeaction.html")




