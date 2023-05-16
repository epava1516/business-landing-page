from django.views.generic import TemplateView
from backend.home.models import Home
from backend.about.models import About, Why, Skill
from backend.services.models import Services, Cta
from backend.portfolio.models import Portfolio
from backend.team.models import Team

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
        return context
