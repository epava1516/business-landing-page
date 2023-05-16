from django.views.generic import TemplateView
from backend.home.models import Home
from backend.about.models import About, Why, Skill
from backend.services.models import Services, Cta

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home'] = Home.objects.first()  # Suponiendo que Home es un SingletonModel
        context['about'] = About.objects.first()
        context['why'] = Why.objects.first()
        context['skill'] = Skill.objects.first()
        context['services'] = Services.objects.first()
    #     context['team'] = Team.objects.all()
        return context
