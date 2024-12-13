from django.contrib import admin
from django.urls import path, include
from projects.views import MaterialListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
    path('api/materials/', MaterialListView.as_view(), name='material_list'), 
]
