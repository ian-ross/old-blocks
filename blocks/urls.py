from django.urls import path

from . import views

app_name = 'blocks'
urlpatterns = [
    path(route='',
         view=views.HomeView.as_view(),
         name='home'),
    
    path(route='projects/',
         view=views.ProjectListView.as_view(),
         name='project_list'),
    
    path(route='settings/',
         view=views.SettingsView.as_view(),
         name='settings'),
]
