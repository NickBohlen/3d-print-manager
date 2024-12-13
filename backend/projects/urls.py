from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, ProjectList, home, AddMaterialView
from projects.views import MaterialListView
from .views import ProjectUploadView
from . import views

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('', include(router.urls)),
    path('', views.home, name='home'),
    path('materials/', views.material_list, name='material_list'),
    path('materials/add/', views.add_material, name='add_material'),
    path('api/projects/', views.ProjectList.as_view(), name='project_list'),
    path('api/materials/add/', AddMaterialView.as_view(), name='add_material_api'),
    path('api/materials/', MaterialListView.as_view(), name='material_list'),
    path('api/projects/upload/', ProjectUploadView.as_view(), name='project-upload'),
]
