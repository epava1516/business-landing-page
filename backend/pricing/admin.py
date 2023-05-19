from django.contrib import admin
from backend.pricing.models import Pricing, Action, PricingColumn, ActionItem

class ActionItemInline(admin.TabularInline):
    model = ActionItem
    extra = 1

class PricingColumnAdmin(admin.ModelAdmin):
    inlines = [ActionItemInline]

class PricingAdmin(admin.ModelAdmin):
    pass

class ActionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pricing, PricingAdmin)
admin.site.register(Action, ActionAdmin)
admin.site.register(PricingColumn, PricingColumnAdmin)
