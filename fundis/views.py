from django.shortcuts import render

def index(request):
    """
    Returns Default Homepage
    """
    return render(request, "index.html")


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def privacy(request):
    return render(request, 'privacy.html')


def terms(request):
    return render(request, 'terms.html')
