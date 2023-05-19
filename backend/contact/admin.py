from django.contrib import admin
from backend.contact.models import Contact, Card

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('description',)

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('location', 'email', 'phone',)
