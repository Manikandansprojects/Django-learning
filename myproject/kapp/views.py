from django.http import HttpResponse
from django.shortcuts import render

def custom_page_not_found(request, exception):
    return render(request, '404.html', status=404)

def home(request):
    return HttpResponse(
        "Hello DJango, You make me frustated<br>"
        "We learning DJango"
    ) 

