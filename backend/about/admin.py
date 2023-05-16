from django.contrib import admin
from backend.about.models import AboutList, About, Why, WhyList, Skill, SkillList

@admin.register(AboutList)
class AboutListAdmin(admin.ModelAdmin):
    list_display = ['item',]

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['first_description', 'second_description', 'display_about_list',]

    def display_about_list(self, obj):
        return ", ".join([about_list.item for about_list in obj.list_description.all()])
    display_about_list.short_description = 'About List Items'

@admin.register(WhyList)
class WhyListAdmin(admin.ModelAdmin):
    list_display = ['title', 'description',]

@admin.register(Why)
class WhyAdmin(admin.ModelAdmin):
    list_display = ['title', 'title_bold', 'description', 'display_why_list',]

    def display_why_list(self, obj):
        return ", ".join([why_list.title for why_list in obj.list_description.all()])
    display_why_list.short_description = 'Why List Items'

@admin.register(SkillList)
class SkillListAdmin(admin.ModelAdmin):
    list_display = ['title', 'ratio',]

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'display_skill_list',]

    def display_skill_list(self, obj):
        return ", ".join([skill_list.title for skill_list in obj.list_description.all()])
    display_skill_list.short_description = 'Skill List Items'
