from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import TimeStampedModel

        
# Constraints:
#   * baseline > 0
#   * bonus >= 0
#   * rows > 0

class Project(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    baseline = models.PositiveIntegerField()
    bonus = models.PositiveIntegerField()
    rows = models.PositiveIntegerField()

    class Meta:
        unique_together = ('user', 'name')

    
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
        