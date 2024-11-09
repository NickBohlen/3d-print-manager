from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet
from . import views

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('materials/', views.material_list, name='material_list'),
    path('materials/add/', views.add_material, name='add_material'),
]
