from django.contrib import admin
from backend.portfolio.models import Portfolio, PortfolioItemList

@admin.register(PortfolioItemList)
class PortfolioItemListAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'img_url', 'type',]

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['description', 'display_portfolio_list',]

    def display_portfolio_list(self, obj):
        return ", ".join([portfolio_list.title for portfolio_list in obj.list_description.all()])
    display_portfolio_list.short_description = 'Portfolio List Items'
