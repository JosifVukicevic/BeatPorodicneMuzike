from django.urls import path
from . import views
from .views import subscribe, success_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('angazujMe/', views.angazujMe, name='angazujMe'),
    path('concerts/', views.concerts, name='concerts'),
    path('gallery/', views.gallery, name='gallery'),
    path('numere/', views.numere, name='numere'),
    path('subscribe/', subscribe, name='subscribe'),
    path('success/', success_view, name='success'),
    path('kontakt', views.kontakt, name='kontakt'),
    path('angazuj_muzicara', views.angazuj_muzicara, name='angazuj_muzicara')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
