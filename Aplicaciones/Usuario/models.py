from django.db import models

# Create your models here.


class Level(models.Model):
    name = models.CharField(max_length=50)

class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    document = models.PositiveSmallIntegerField()
    level = models.ForeignKey(Level, on_delete.set_NULL)

def __str__(self):
        texto = "{0}"
        return texto.format(self.user)