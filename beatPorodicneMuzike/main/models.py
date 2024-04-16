from django.db import models

class SlikeNastupi(models.Model):
    naziv = models.CharField(max_length=100)
    slika = models.ImageField(upload_to='slike/')
    opis = models.TextField(blank=True)
    kategorija = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.naziv

class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"Novi subscribe korisnik: {self.email}"

class Angazovanje(models.Model):
    ime_prezime = models.CharField(max_length=100)
    mjesto_zurke = models.CharField(max_length=100)
    vrijeme = models.CharField(max_length=50)
    datum = models.DateField()
    email = models.EmailField()
    telefon = models.CharField(max_length=20)
    muzicar = models.CharField(max_length=50)

    def __str__(self):
        return f"Angazovanje za datum: {self.datum} od korisnika: {self.ime_prezime}"

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Poruka od {self.full_name}"
"""
class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    image = models.ImageField(upload_to='imagesForSongs/')
    audio_file = models.FileField(upload_to='songs/')

    def __str__(self):
        return f"Numera: {self.title}"
"""
class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    image = models.ImageField(upload_to='imagesForSongs/')
    audio_file = models.FileField(upload_to='songs/')
    allow_download = models.BooleanField(default=True)

    def __str__(self):
        return f"Numera: {self.title}"


class Media(models.Model):
    IMAGE = 'IMG'
    VIDEO = 'VID'
    MEDIA_TYPES = [
        (IMAGE, 'Image'),
        (VIDEO, 'Video'),
    ]

    naziv = models.CharField(max_length=100)
    opis = models.TextField()
    tip = models.CharField(max_length=3, choices=MEDIA_TYPES, default=IMAGE)
    media_file = models.FileField(upload_to='media_files/')
    kategorija = models.CharField(max_length=50)

    def __str__(self):
        return f"Media: {self.naziv}, Tip: {self.tip}, Opis: {self.opis}"
