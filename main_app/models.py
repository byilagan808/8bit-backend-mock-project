from django.db import models

# Create your models here.
class File(models.Model): 
    bytes = models.TextField() 
    filename = models.CharField(max_length=255) 
    mimetype = models.CharField(max_length=50) 

    def __str__(self): 
        return self.filename

class MiscImage(models.Model): 
    name = models.CharField(max_length=100) 
    image = models.ImageField(upload_to='main_app.File/bytes/filename/mimetype', null=True,help_text="Please compress image and convert type to webp before uploading. https://imagecompressor.com/, https://cloudconvert.com/webp-converter") 

    def __str__(self): 
        return self.name

    def delete(self, *args, **kwargs): 
        super(MiscImage, self).delete(*args, **kwargs)
        File.objects.filter(filename = self.image.name).delete()
