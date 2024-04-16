from django import forms
from .models import Subscriber, Angazovanje, ContactMessage

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
"""
class AngazujMuzicaraForma(forms.ModelForm):
    class Meta:
        model = Angazovanje
        fields = ['ime_prezime', 'mjesto_zurke', 'vrijeme', 'datum', 'email', 'telefon', 'muzicar']
"""
class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)
    message = forms.CharField(widget=forms.Textarea)
