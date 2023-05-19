from django.views.generic import TemplateView
from backend.home.models import Home
from backend.about.models import About, Why, Skill
from backend.services.models import Services, Cta
from backend.portfolio.models import Portfolio
from backend.team.models import Team
from backend.faq.models import Faq
from backend.contact.models import Contact, Card
from backend.pricing.models import Pricing, PricingColumn

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home'] = Home.objects.first()
        context['about'] = About.objects.first()
        context['why'] = Why.objects.first()
        context['skill'] = Skill.objects.first()
        context['services'] = Services.objects.first()
        context['cta'] = Cta.objects.first()
        context['portfolio'] = Portfolio.objects.first()
        context['team'] = Team.objects.first()
        context['faq'] = Faq.objects.first()
        context['contact'] = Contact.objects.first()
        context['card'] = Card.objects.first()
        context['pricing'] = Pricing.objects.first()
        context['columns'] = PricingColumn.objects.filter(pricing=context['pricing'])
        return context
