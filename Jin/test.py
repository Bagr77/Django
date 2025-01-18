from django.db import models


# Create your models here.

class Auto(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField()
    price = models.IntegerField(default=0, blank=True)
    distance = models.IntegerField(default=0, blank=True)
    is_exists = models.BooleanField(default=True)

    def __str__(self):
        return self.title



cars = [
    dict(name="BMW X6", model="BMW", price=6000111),
    dict(name="Toyota Corolla", model="Toyota", distance=72000),
    dict(name="Haval 7", model="Haval", price=3500222)
]

for m in cars:
    Auto.objects.create(**m)

autos = Auto.objects.all()[:2]
