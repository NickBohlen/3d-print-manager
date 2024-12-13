from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    material_type = models.CharField(max_length=100)
    stl_file = models.FileField(upload_to='uploads/')  # This is where the .stl file will be stored
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Material(models.Model):
    MATERIAL_TYPES = [
        ('PLA', 'PLA'),
        ('ABS', 'ABS'),
        ('PETG', 'PETG'),
    ]
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=MATERIAL_TYPES)
    color = models.CharField(max_length=30)
    initial_quantity = models.DecimalField(max_digits=6, decimal_places=2, help_text="Quantity in grams")
    current_quantity = models.DecimalField(max_digits=6, decimal_places=2)
    reorder_threshold = models.DecimalField(max_digits=6, decimal_places=2, help_text="Low stock threshold in grams")

    def __str__(self):
        return f"{self.color} {self.type} ({self.current_quantity}g remaining)"

class PrintJob(models.Model):
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True)
    estimated_material_usage = models.DecimalField(max_digits=6, decimal_places=2, help_text="Material usage in grams")

    def complete_print(self):
        if self.material and self.estimated_material_usage:
            self.material.current_quantity -= self.estimated_material_usage
            self.material.save()
            # Check if material is below reorder threshold
            if self.material.current_quantity <= self.material.reorder_threshold:
                print(f"Low stock alert: {self.material} needs to be reordered!")
