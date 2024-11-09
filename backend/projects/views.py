from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer
from django.shortcuts import render, redirect
from .models import Material

def material_list(request):
    materials = Material.objects.all()
    return render(request, 'material_list.html', {'materials': materials})

def add_material(request):
    if request.method == "POST":
        name = request.POST['name']
        material_type = request.POST['type']
        color = request.POST['color']
        initial_quantity = request.POST['initial_quantity']
        reorder_threshold = request.POST['reorder_threshold']
        Material.objects.create(
            name=name, type=material_type, color=color,
            initial_quantity=initial_quantity,
            current_quantity=initial_quantity,
            reorder_threshold=reorder_threshold
        )
        return redirect('material_list')
    return render(request, 'add_material.html')

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
