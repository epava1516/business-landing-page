from django.db import models
from backend.home.models import SingletonModel
from geopy.geocoders import Nominatim

# Create your models here.
class Contact(SingletonModel):
    description = models.TextField()

    def __str__(self):
        return self.description[:50]

class Card(SingletonModel):
    location = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, db_index=True)
    phone = models.CharField(max_length=50, db_index=True)
    maps = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.location} {self.email} {self.phone}"

    def save(self, *args, **kwargs):
        geolocator = Nominatim(user_agent="syaas_consulting")
        geolocation = geolocator.geocode(self.location)
        if geolocation:
            self.maps = f"//maps.google.com/maps?q={geolocation.latitude},{geolocation.longitude}&z=16&output=embed" # type: ignore
        else:
            print(f"No se pudo geocodificar la ubicación: {self.location}")
            self.maps = None
        super().save(*args, **kwargs)