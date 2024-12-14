from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Material, PrintJob, PrintError, StandaloneSTL, STLFile
from .forms import MaterialForm, PrintJobForm, PrintErrorForm, StandaloneSTLForm, STLFileForm
from django.conf import settings
import cv2
from django.http import StreamingHttpResponse
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

@login_required
def home(request):
    # Fetch errors with the status 'In Progress'
    in_progress_errors = PrintError.objects.filter(status='In Progress')

    # Fetch other required data
    materials = Material.objects.all()
    print_jobs = PrintJob.objects.all()
    stl_files = STLFile.objects.all()

    return render(request, 'home.html', {
        'in_progress_errors': in_progress_errors,
        'materials': materials,
        'print_jobs': print_jobs,
        'stl_files': stl_files,
    })

@login_required
def add_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MaterialForm()
    return render(request, 'add_material.html', {'form': form})

@login_required
def add_print_job(request):
    if request.method == 'POST':
        form = PrintJobForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('all_print_jobs')  # Redirect to the all print jobs page after saving
        else:
            # Add logging or print statements here if you want to debug form errors
            print(form.errors)
    else:
        form = PrintJobForm()

    return render(request, 'add_print_job.html', {'form': form})

@login_required
def all_print_jobs(request):
    print_jobs = PrintJob.objects.all()  # Get all print jobs
    return render(request, 'all_print_jobs.html', {'print_jobs': print_jobs})

@login_required
def update_print_job(request, pk):
    print_job = get_object_or_404(PrintJob, pk=pk)
    if request.method == 'POST':
        form = PrintJobForm(request.POST, instance=print_job)
        if form.is_valid():
            form.save()
            return redirect('all_print_jobs')
    else:
        form = PrintJobForm(instance=print_job)
    return render(request, 'update_print_job.html', {'form': form})

@login_required
def remove_print_job(request, pk):
    print_job = get_object_or_404(PrintJob, pk=pk)
    if request.method == 'POST':
        print_job.delete()
        return redirect('all_print_jobs')
    return render(request, 'all_print_jobs.html')

@login_required
def all_print_errors(request):
    errors = PrintError.objects.all().order_by('-timestamp')  # Fetching all errors, ordered by most recent
    return render(request, 'all_print_errors.html', {'errors': errors})

@login_required
def add_print_error(request):
    if request.method == 'POST':
        form = PrintErrorForm(request.POST)
        if form.is_valid():
            form.save()  # Save the print error with the selected status
            return redirect('all_print_errors')  # Redirect after successful form submission
    else:
        form = PrintErrorForm()

    return render(request, 'add_print_error.html', {'form': form})

@login_required
def upload_stl(request):
    if request.method == 'POST' and request.FILES:
        # If the form is submitted and contains files
        form = STLFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the STL file to the database
            return redirect('stl_files')  # Redirect to the STL files page
    else:
        form = STLFileForm()

    return render(request, 'upload_stl.html', {'form': form})

@login_required
def stream_video(request):
    stream_url = os.path.join(settings.MEDIA_URL, 'streams/stream.m3u8')
    return render(request, 'streaming.html', {'stream_url': stream_url})

RTSP_URL = 'rtsp://A8Rd5dWFSkMr:5v57qAEce4em@192.168.0.14:554/live0'

@login_required
def generate_frame():
    cap = cv2.VideoCapture(RTSP_URL)
    if not cap.isOpened():
        raise RuntimeError("Unable to open RTSP stream. Check the URL and camera settings.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@login_required
def stream_video(request):
    return StreamingHttpResponse(generate_frame(),
                                 content_type='multipart/x-mixed-replace; boundary=frame')

@login_required
def streaming_page(request):
    return render(request, 'streaming.html')

@login_required
def all_materials(request):
    materials = Material.objects.all()

    if request.method == 'POST':
        selected_material_id = request.POST.get('selected_material')
        action = request.POST.get('action')

        if selected_material_id:
            material = get_object_or_404(Material, id=selected_material_id)

            if action == 'update':
                # Redirect to the edit page for the selected material with the correct material_id
                return redirect('edit_material', material_id=material.id)
            elif action == 'delete':
                # Delete the selected material
                material.delete()
                return redirect('all_materials')

    return render(request, 'all_materials.html', {'materials': materials})

@login_required
def edit_material(request, material_id):
    material = get_object_or_404(Material, id=material_id)

    if request.method == 'POST':
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('all_materials')
    else:
        form = MaterialForm(instance=material)

    return render(request, 'edit_material.html', {'form': form, 'material': material})

@login_required
def remove_material(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    material.delete()
    return redirect('all_materials')

@login_required
def stl_files(request):
    # Query all STL files from the database
    stl_files = STLFile.objects.all()
    return render(request, 'stl_files.html', {'stl_files': stl_files})

@login_required
def remove_stl(request, stl_id):
    stl_file = get_object_or_404(STLFile, id=stl_id)
    stl_file.delete()
    return redirect('stl_files')  # Redirect back to the STL files list

@login_required
def remove_print_error(request, error_id):
    error = get_object_or_404(PrintError, id=error_id)
    
    if request.method == 'POST':
        error.delete()  # This removes the print error from the database.
        return redirect('all_print_errors')  # Redirect back to the print errors page.

    return redirect('all_print_errors')

@login_required
def change_print_error_status(request, error_id):
    error = get_object_or_404(PrintError, id=error_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        error.status = new_status
        error.save()
    return redirect('all_print_errors')

@login_required
def update_print_error_status(request, error_id):
    try:
        error = PrintError.objects.get(id=error_id)
    except PrintError.DoesNotExist:
        raise Http404("Print error not found")

    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in ['Pending', 'Resolved', 'In Progress']:
            error.status = new_status
            error.save()
        return redirect('all_print_errors')  # Redirect back to the errors page

    return redirect('all_print_errors')  # Redirect back if not a POST request

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('login')  # Redirect to the home page after signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html' 