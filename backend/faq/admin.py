from django.contrib import admin
from backend.faq.models import Faq, FaqList

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['description',]

@admin.register(FaqList)
class FaqListAdmin(admin.ModelAdmin):
    list_display = ['title', 'description',]
