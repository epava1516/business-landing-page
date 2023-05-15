from django.contrib import admin
from backend.portfolio.models import Portfolio, PortfolioItemList

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['description',]

@admin.register(PortfolioItemList)
class PortfolioItemListAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'img_url', 'type',]
