from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name='blocks/home.html'
    
class ProjectListView(TemplateView):
    template_name='blocks/project_list.html'
    
class SettingsView(TemplateView):
    template_name='blocks/settings.html'
