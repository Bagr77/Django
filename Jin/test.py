from django.db import models


# Create your models here.

class Auto(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField()
    price = models.IntegerField(default=0, blank=True)
    is_exists = models.BooleanField(default=True)

    def __str__(self):
        return self.title


Auto.objects.create(name="BWM X6", model="BMW", price=6000111)
Auto.objects.create(name="Toyota Corolla", model="Toyota")
Auto.objects.create(name="Haval 7", model="Haval", price=3500222)

autos = Auto.objects.all()[0]


