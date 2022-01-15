from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import View, DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Project, TimeBlock
from .forms import ProjectCreateForm, ProjectUpdateForm, TimeBlockUpdateForm
from .helpers import project_grid_data
from .preferences import BLOCK_SIZE


class HomeView(LoginRequiredMixin, TemplateView):
    template_name='blocks/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['block_size'] = BLOCK_SIZE
        blocks = Project.objects.week_blocks(self.request.user)
        projects = Project.objects.filter(user=self.request.user, active=True)
        context['project_list'] = [project_grid_data(p, blocks[p.name]) for p in projects]
        return context


class ProjectListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    
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


class ProjectReorderView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        Project.objects.reorder(kwargs['pk'], kwargs['dir'])
        return HttpResponseRedirect(reverse('blocks:project_list'))


class TimeBlockUpdateView(LoginRequiredMixin, UpdateView):
    model = TimeBlock
    form_class = TimeBlockUpdateForm
    success_url = reverse_lazy('blocks:home')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper.form_action = reverse('blocks:block_update', kwargs={'pk': form.instance.pk})
        return form


class TimeBlockDeleteView(LoginRequiredMixin, DeleteView):
    model = TimeBlock
    success_url = reverse_lazy('blocks:home')


class TimerView(LoginRequiredMixin, TemplateView):
    template_name = 'blocks/timer.html'
