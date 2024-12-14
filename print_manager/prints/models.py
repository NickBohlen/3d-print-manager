from django.db import models

class Material(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.color}"

class PrintJob(models.Model):
    STATUS_CHOICES = [
        ('Queued', 'Queued'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    model_file = models.FileField(upload_to='prints/')
    estimated_time = models.DurationField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Queued')
    material = models.ForeignKey('Material', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.model_file.name} ({self.status})"
    
class PrintError(models.Model):
    ERROR_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Resolved', 'Resolved'),
        ('In Progress', 'In Progress'),
    ]

    print_job = models.ForeignKey('PrintJob', on_delete=models.CASCADE, default=1)  # Assuming PrintJob model exists
    error_message = models.TextField()
    status = models.CharField(max_length=20, choices=ERROR_STATUS_CHOICES, default='Pending')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Error in {self.print_job.model_file.name}: {self.error_message[:30]}"
    
class StandaloneSTL(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='stl_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class STLFile(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='stl_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name