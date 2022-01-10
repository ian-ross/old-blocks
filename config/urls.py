from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('magiclink.urls', namespace='magiclink')),
    path('', include('blocks.urls', namespace='blocks')),
    
    path('__debug__/', include('debug_toolbar.urls')),
]
