from django.urls import path, register_converter

from .views import HomeView
from .views import ProjectListView, ProjectReorderView
from .views import ProjectCreateView, ProjectUpdateView, ProjectDeleteView

from .converters import DirectionConverter


register_converter(DirectionConverter, 'dir')

app_name = 'blocks'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/add/', ProjectCreateView.as_view(), name='project_add'),
    path('projects/<int:pk>/', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('projects/<int:pk>/reorder/<dir:dir>/', ProjectReorderView.as_view(), name='project_reorder'),
]
