from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listin']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        #check already inquired user
        has_contacted = Contact.objects.all().filter(listing_id=listing_id, name=name, email=email, phone=phone)
        if has_contacted:
            messages.error(request, 'You have already inquired for this property')
            return redirect('/listings/'+listing_id)
        

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
            phone=phone, message=message,)

        contact.save()

        messages.success(request, 'Your request has been submitted, we will get back to you soon')

        return redirect('/listings/'+listing_id)

    
