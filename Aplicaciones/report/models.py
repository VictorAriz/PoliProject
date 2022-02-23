from django.db import models

# Create your models here.

class Report(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=50)
    description = models.TextField()
    text = models.CharField(max_length=50, null=True)
    image = models.ImageField("txtImagen", upload_to='media/', max_length=255, null=True, blank=True)
    # archive = models.FileField(("Archivo"), upload_to='Archivos/', null=True)


    def __str__(self):
        texto = "{0}"
        return texto.format(self.name)