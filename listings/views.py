from django.shortcuts import render, get_object_or_404
from .models import Listings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):
    listings = Listings.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 2)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings' : paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listings, pk=listing_id)

    context = {
        'listing' : listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    return render(request, 'listings/search.html')
