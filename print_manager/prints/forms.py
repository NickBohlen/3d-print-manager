from django import forms
from .models import Material, PrintJob, PrintError, StandaloneSTL, STLFile

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'type', 'color', 'quantity']

class PrintJobForm(forms.ModelForm):
    class Meta:
        model = PrintJob
        fields = ['material', 'model_file', 'estimated_time', 'status']  # Ensure 'material' is in the fields list
    
    material = forms.ModelChoiceField(queryset=Material.objects.all(), empty_label="Select Material")

class PrintErrorForm(forms.ModelForm):
    ERROR_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Resolved', 'Resolved'),
        ('In Progress', 'In Progress'),
    ]
    
    status = forms.ChoiceField(choices=ERROR_STATUS_CHOICES, initial='Pending')

    class Meta:
        model = PrintError
        fields = ['print_job', 'error_message', 'status']  

class StandaloneSTLForm(forms.ModelForm):
    class Meta:
        model = StandaloneSTL
        fields = ['name', 'file']

class STLFileForm(forms.ModelForm):
    class Meta:
        model = STLFile
        fields = ['name', 'file'] 

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'color', 'quantity']