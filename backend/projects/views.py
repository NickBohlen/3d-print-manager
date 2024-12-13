from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework import viewsets
from .models import Material, Project
from .serializers import MaterialSerializer, ProjectSerializer
from django.shortcuts import render, redirect
from .forms import MaterialForm

def home(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the same page after saving the form
    else:
        form = MaterialForm()

    materials = Material.objects.all()  # Get all materials from the database
    return render(request, 'home.html', {'form': form, 'materials': materials})

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

class AddMaterialView(APIView):
    def post(self, request):
        serializer = MaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MaterialListView(APIView):
    def get(self, request):
        materials = Material.objects.all()
        serializer = MaterialSerializer(materials, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = MaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        """
        Get the list of all projects or a single project based on provided ID.
        """
        # If an ID is provided, retrieve that project
        if 'id' in kwargs:
            try:
                project = Project.objects.get(pk=kwargs['id'])
                serializer = ProjectSerializer(project)
                return Response(serializer.data)
            except Project.DoesNotExist:
                return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            # If no ID is provided, return a list of all projects
            projects = Project.objects.all()
            serializer = ProjectSerializer(projects, many=True)
            return Response(serializer.data)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectList(APIView):
    def get(self, request):
        projects = Project.objects.all()
        projects_data = [{"name": project.name, "description": project.description} for project in projects]
        return Response(projects_data, status=status.HTTP_200_OK)
    
    
def home(request):
    # Query all materials from the database
    materials = Material.objects.all()

    # Render the template with the materials data
    return render(request, 'home.html', {'materials': materials})