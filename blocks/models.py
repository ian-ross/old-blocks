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


# TODO: NEED A CUSTOM MANAGER HERE TO DO TYPE CONVERSION

class Setting(TimeStampedModel):
    class Type(models.TextChoices):
        BLOCK_SIZE = 'BLOCK_SIZE', _('Block size (pixels)')
        PROJECT_FONT = 'PROJECT_FONT', _('Project title font')
        BASELINE_COLOUR = 'BASELINE_COLOUR', _('Baseline cell background colour')
        BONUS_COLOUR = 'BONUS_COLOUR', _('Bonus cell background colour')
        BORDER_COLOUR = 'BORDER_COLOUR', _('Cell border colour')
        DAY_COLOURS = 'DAY_COLOURS', _('Colours for each weekday (Monday-Sunday)')
        BLOCK_LENGTH = 'BLOCK_LENGTH', _('Length of block (minutes)')
        COMPLETION_SOUND = 'COMPLETION_SOUND', _('Play sound on block completion?')
        COMPLETION_NOTIFICATION = 'COMPLETION_NOTIFICATION', _('Browser notification on block completion?')
        
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    key = models.CharField(max_length=32, choices=Type.choices)
    raw_value = models.CharField(max_length=255)

    def value(self):
        if self.key in [Type.BLOCK_SIZE, Type.BLOCK_LENGTH]:
            return int(self.raw_value)
        elif self.key in [Type.COMPLETION_SOUND, Type.COMPLETION_NOTIFICATION]:
            return self.raw_value == 'true'
        elif self.key == Type.DAY_COLOURS:
            return self.raw_value.split(',')
        else:
            return self.raw_value
        