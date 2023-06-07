# from django.http import HttpResponse
from listings.models import Band, Listing
from django.shortcuts import render
from listings.forms import ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect
from listings.forms import ContactUsForm, BandForm, ListingForm
from django.urls import reverse


def band_list(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/band_list.html',
                  {'bands': bands})


def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band})

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    
    else:
        form = BandForm()

    return render (request,
        'listings/band_create.html',
        {'form': form})

def band_update(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
        return redirect('band-detail',band.id)
    else:
        form = BandForm(instance=band)  # on pré-remplir le formulaire avec un groupe existant
    return render(request,
                'listings/band_update.html',
                {'form': form})
def band_delete(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        band.delete()
        return redirect('band_list')
    
    return render(request,
                  'listings/band_delete.html',
                  {'band': band})   


def listing_list(request):
    listings = Listing.objects.all()
    return render(request,
                  'listings/listing_list.html',
                  {'listings': listings})


def listing_detail(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    return render(request,
                  'listings/listing_detail.html',
                  {'listing': listing})

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail', listing.id)
    
    else:
        form = ListingForm()

    return render (request,
        'listings/listing_create.html',
        {'form': form})

def listing_update(request, id):
    listing = Listing.objects.get(id=id)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
        return redirect('listing-detail',listing.id)
    else:
        form = ListingForm(instance=listing)  # on pré-remplir le formulaire avec un groupe existant
    return render(request,
                'listings/listing_update.html',
                {'form': form})


def about(request):
    return render(request,
                  'listings/about.html',
                  )


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonymouse"} via MerchEx Contact us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['diarrassoubaibra58@gmail.com'],
            )
            return redirect('/email_sent/')
    else:
        form = ContactUsForm()
    return render(request, 'listings/contact.html', {'form': form})


def email_sent(request):
    return render(request, 'listings/email_sent.html')
