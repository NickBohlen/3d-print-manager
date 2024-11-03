from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    material = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
