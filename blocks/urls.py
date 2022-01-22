from django.urls import path, register_converter

from .views import HomeView, EmailNotAllowedView
from .views import ProjectListView, ProjectReorderView
from .views import ProjectCreateView, ProjectUpdateView, ProjectDeleteView
from .views import TimeBlockUpdateView, TimeBlockDeleteView
from .views import TimerView, create_block

from .converters import DirectionConverter


register_converter(DirectionConverter, 'dir')

app_name = 'blocks'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('email_not_allowed', EmailNotAllowedView.as_view(), name='email_not_allowed'),
    
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/add/', ProjectCreateView.as_view(), name='project_add'),
    path('projects/<int:pk>/', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('projects/<int:pk>/reorder/<dir:dir>/', ProjectReorderView.as_view(), name='project_reorder'),

    path('blocks/create/', create_block, name='block_create'),
    path('blocks/add/<int:project_id>/<int:row>/<int:column>/', TimerView.as_view(), name='block_add_cell'),
    path('blocks/add/<int:project_id>/', TimerView.as_view(), name='block_add'),
    path('blocks/<int:pk>/', TimeBlockUpdateView.as_view(), name='block_update'),
    path('blocks/<int:pk>/delete/', TimeBlockDeleteView.as_view(), name='block_delete'),
]
