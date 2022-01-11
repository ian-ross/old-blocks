from django.urls import path

from .views import HomeView
from .views import ProjectListView
from .views import ProjectCreateView, ProjectUpdateView, ProjectDeleteView
from .views import SettingsView

app_name = 'blocks'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/add/', ProjectCreateView.as_view(), name='project_add'),
    path('projects/<int:pk>/', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    
    path('settings/', SettingsView.as_view(), name='settings'),
]
