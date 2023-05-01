from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    detail = models.TextField(max_length = 500, blank=True)
    
    def __str__(self):
        return self.title