from django.db import models

# Create your models here.

class ShopItem(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField(blank=True, default=0)
    price = models.IntegerField(default=0)
    is_exists = models.BooleanField(default=True)

    def __str__(self):
        return self.title
