from django.shortcuts import render
from listings.models import Listings

def index(request):

    listings = Listings.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings' : listings
    }

    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')