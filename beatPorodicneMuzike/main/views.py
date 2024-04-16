from django.utils import timezone
from django.shortcuts import render, redirect
from .models import SlikeNastupi, ContactMessage, Angazovanje, Song, Media
from .forms import SubscriberForm, ContactForm


def home(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def angazujMe(request):
    return render(request, 'angazujMe.html', {})

def concerts(request):
    slike = SlikeNastupi.objects.all()
    return render(request, 'concerts.html', {'slike': slike})

def gallery(request):
    slike_i_video = Media.objects.all()
    return render(request, 'gallery.html', {'slike_i_video': slike_i_video})

def numere(request):
    songs = Song.objects.all()
    return render(request, 'numere.html', {'songs': songs})

def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SubscriberForm()
    return render(request, 'subscribe.html', {'form': form})

def success_view(request):
    return render(request, 'subscribe.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            ContactMessage.objects.create(
                full_name=full_name,
                email=email,
                phone_number=phone_number,
                message=message
            )
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})


def kontakt(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            message=message,
            created_at=timezone.now()
        )

        return redirect('success')

    return render(request, 'index.html')

def angazuj_muzicara(request):
    if request.method == 'POST':
        ime_prezime = request.POST.get('ime_prezime')
        mjesto_zurke = request.POST.get('mjesto_zurke')
        vrijeme = request.POST.get('vrijeme')
        datum = request.POST.get('datum')
        email = request.POST.get('email')
        telefon = request.POST.get('telefon')
        muzicar = request.POST.get('muzicar')

        Angazovanje.objects.create(
            ime_prezime=ime_prezime,
            mjesto_zurke=mjesto_zurke,
            vrijeme=vrijeme,
            datum=datum,
            email=email,
            telefon=telefon,
            muzicar=muzicar
        )

        return redirect('success')

    return render(request, 'index.html')