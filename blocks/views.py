from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Project
from .forms import ProjectCreateForm, ProjectUpdateForm


class HomeView(LoginRequiredMixin, TemplateView):
    template_name='blocks/home.html'


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project

    
class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectUpdateForm
    success_url = reverse_lazy('blocks:project_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper.form_action = reverse('blocks:project_update', kwargs={'pk': form.instance.pk})
        return form
    
    
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectCreateForm
    success_url = reverse_lazy('blocks:project_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.active = True
        return super().form_valid(form)

    
class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('blocks:project_list')

    
class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'blocks/settings.html'
