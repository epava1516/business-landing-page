from django.views.generic import TemplateView
from backend.home.models import Home
from backend.about.models import About, AboutList, Why, WhyList, Skill, SkillList

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home'] = Home.objects.first()  # Suponiendo que Home es un SingletonModel
        context['about'] = About.objects.first()
        print(context['about'].list_description.all())
    #     context['team'] = Team.objects.all()
        return context
