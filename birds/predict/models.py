from django.db import models

# Create your models here.

class Bird(models.Model):
    name = models.CharField(max_length = 50)
    image = models.CharField(max_length = 300)
    number = models.CharField(max_length = 4)
    description = models.CharField(max_length = 1000)

    def __str__(self):
        return self.name