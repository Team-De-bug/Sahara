from django.db import models


# Create your models here.
class Stock(models.Model):
    product_name = models.CharField(max_length=100, name="product_name")
    cost = models.IntegerField(name="cost")
    rating = models.IntegerField(name="rating")

    def __str__(self):
        return self.product_name
