# forms.py
from django import forms
from .models import Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'type', 'color', 'initial_quantity', 'current_quantity', 'reorder_threshold']