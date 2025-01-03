from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contacts
from django.core.mail import send_mail


def contacts(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        
            
        contacts = Contacts(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)
        contacts.save()
        # Send mail
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for '+listing+'. \n Message: '+message+'',
            'susanna0liu@gmail.com',
            [
                # realtor_email,
                'susanna0liu@gmail.com'],
            fail_silently=False
            )

        messages.success(request,'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/listings/'+listing_id)