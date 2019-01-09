from django.shortcuts import render
from listings.models import Listings
from listings.choices import price_choices, bedroom_choices, state_choices 

def index(request):

    listings = Listings.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings' : listings,
        'bedroom_choices' : bedroom_choices,
        'price_choices': price_choices
    }

    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
