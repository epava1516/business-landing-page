from django.contrib import admin
from backend.faq.models import Faq, FaqList

@admin.register(FaqList)
class FaqListAdmin(admin.ModelAdmin):
    list_display = ['title', 'description',]

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['description', 'display_faq_list',]

    def display_faq_list(self, obj):
        return ", ".join([faq_list.title for faq_list in obj.list_description.all()])
    display_faq_list.short_description = 'Faq List Items'
