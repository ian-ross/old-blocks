from datetime import datetime, timedelta
import json

from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import View, DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import get_object_or_404

from .models import Project, TimeBlock
from .forms import ProjectCreateForm, ProjectUpdateForm, TimeBlockUpdateForm
from .helpers import project_grid_data
from .preferences import BLOCK_SIZE, BLOCK_DURATION


class HomeView(LoginRequiredMixin, TemplateView):
    template_name='blocks/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['block_size'] = BLOCK_SIZE
        blocks = Project.objects.week_blocks(self.request.user)
        projects = Project.objects.filter(user=self.request.user, active=True)
        context['project_list'] = [project_grid_data(p, blocks[p.name]) for p in projects]
        return context

class EmailNotAllowedView(TemplateView):
    template_name='blocks/email_not_allowed.html'
    
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        project_id = kwargs['project_id']
        if 'row' in kwargs:
            row = kwargs['row']
            column = kwargs['column']
        else:
            row, column = Project.objects.next_cell(project_id)
        
        context['timer_data'] = {
            'url': reverse('blocks:block_create'),
            'project_id': project_id,
            'row': row,
            'column': column,
            'duration': BLOCK_DURATION }
        return context


@require_POST
@login_required
def create_block(request):
    body = json.loads(request.body)
    project = get_object_or_404(Project, pk=body['project_id'])
    start = datetime.strptime(body['start'][0:19], "%Y-%m-%dT%H:%M:%S")
    TimeBlock.objects.create(project=project,
                             start=timezone.make_aware(start),
                             duration=timedelta(seconds=body['duration']),
                             row=body['row'], column=body['column'],
                             note=body['note'])
    return JsonResponse({ 'ok': True })
