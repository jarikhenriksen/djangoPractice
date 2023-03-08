from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    species = models.CharField(max_length=50)

    def __str__(self):
        return self.name
        

