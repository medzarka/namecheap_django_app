from django.shortcuts import render
from .models import Quote


def home(request):
    quotes = Quote.objects.all()
    return render(request, 'web/index.html', {"quotes": quotes})