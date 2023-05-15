from django.contrib import admin
from backend.services.models import Services, ServiceList, Cta

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['description',]

@admin.register(ServiceList)
class ServiceListAdmin(admin.ModelAdmin):
    list_display = ['icon', 'title', 'description',]

@admin.register(Cta)
class CtaAdmin(admin.ModelAdmin):
    list_display = ['title', 'description',]
