from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import TimeStampedModel

        
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

    
class Block(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    start = models.DateTimeField()
    duration = models.DurationField()
