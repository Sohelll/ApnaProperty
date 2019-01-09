from django.contrib import admin

from .models import Listings 

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'zipcode', 'state')
    list_per_page = 20
    


admin.site.register(Listings, ListingAdmin)