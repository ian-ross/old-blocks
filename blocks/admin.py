from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Project, TimeBlock


admin.site.register(User, UserAdmin)
admin.site.register(Project)
admin.site.register(TimeBlock)
