from django.contrib import admin
from backend.services.models import Services, ServiceList, Cta

@admin.register(ServiceList)
class ServiceListAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'icon',]

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['description', 'display_service_list',]

    def display_service_list(self, obj):
        return ", ".join([service_list.title for service_list in obj.list_description.all()])
    display_service_list.short_description = 'About List Items'

@admin.register(Cta)
class CtaAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'button',]
