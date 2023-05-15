from django.contrib import admin
from backend.pricing.models import Pricing, PricingDescriptionList, PricingList

@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ['description',]

@admin.register(PricingDescriptionList)
class PricingDescriptionListAdmin(admin.ModelAdmin):
    list_display = ['title',]

@admin.register(PricingList)
class PricingListAdmin(admin.ModelAdmin):
    list_display = ['title', 'price',]
