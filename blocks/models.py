from collections import namedtuple
from itertools import groupby

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import TimeStampedModel
from .helpers import Week


TimeBlockView = namedtuple('TimeBlockView', ['pk', 'start', 'row', 'column'])


class ProjectManager(models.Manager):
    def reorder(self, project_id, direction):
        project = self.get(pk=project_id)
        order = list(project.user.get_project_order())
        current_pos = order.index(project_id)
        new_pos = current_pos
        if current_pos > 0 and direction == 'up':
            new_pos = current_pos - 1
        elif current_pos < len(order) - 1 and direction == 'down':
            new_pos = current_pos + 1
        order[current_pos], order[new_pos] = order[new_pos], order[current_pos]
        project.user.set_project_order(order)

    def week_blocks(self, user, ts=None):
        week = Week(ts)
        qs = (Project.objects
              .filter(active=True, user=user)
              .filter(timeblock__start__gte=week.start(),
                      timeblock__start__lt=week.end())
              .values_list('name', 'timeblock__pk', 'timeblock__start',
                           'timeblock__row', 'timeblock__column')
              .order_by('_order', 'timeblock__row', 'timeblock__column'))
        
        info = {}
        for k, g in groupby(qs, lambda t: t[0]):
            info[k] = list(map(lambda t: TimeBlockView(pk=t[1], start=t[2], row=t[3], column=t[4]), g))

        result = {}
        for p in self.filter(active=True, user=user):
            if p.name in info:
                result[p.name] = info[p.name]
            else:
                result[p.name] = []
        
        return result
        

class Project(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    baseline = models.PositiveIntegerField()
    bonus = models.PositiveIntegerField(default=0)
    rows = models.PositiveIntegerField(default=1)
    active = models.BooleanField(default=True)

    objects = ProjectManager()

    class Meta:
        order_with_respect_to = 'user'
        constraints = [
            models.UniqueConstraint(fields=('user', 'name'), name='unique_name'),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blocks:project_update', kwargs={'pk': self.pk})

    
class TimeBlock(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    start = models.DateTimeField()
    duration = models.DurationField()
    row = models.PositiveIntegerField()
    column = models.PositiveIntegerField()
    note = models.TextField(blank=True)
    