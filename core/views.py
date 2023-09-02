from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home")

def search(request):
    query = None
    if 'q' in request.GET:
        query = request.GET['q']
    return render(request, 'search.html', {'query': query})