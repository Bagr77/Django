from django.db import models
from django import forms


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

# username: текстовое поле; максимальная длина 100 символов, обязательное;
# email: поле ввода адреса электронной почты; обязательное;
# agree: поле типа CheckBox; обязательное;
# content: поле ввода полноценного многострочного текста; обязательное.

class CommentForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    agree = forms.BooleanField()
    content = forms.CharField(widget=forms.Textarea)
