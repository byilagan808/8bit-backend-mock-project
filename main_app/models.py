from django.db import models

# Create your models here.
class File(models.Model): 
    bytes = models.TextField() 
    filename = models.CharField(max_length=255) 
    mimetype = models.CharField(max_length=50) 

    def __str__(self): 
        return self.filename

