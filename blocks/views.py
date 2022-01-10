from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):
    template_name='blocks/home.html'
    
class ProjectListView(LoginRequiredMixin, TemplateView):
    template_name='blocks/project_list.html'
    
class SettingsView(LoginRequiredMixin, TemplateView):
    template_name='blocks/settings.html'
