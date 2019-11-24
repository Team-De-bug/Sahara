from django.db import models


# Create your models here.
class Stock(models.Model):
    product_name = models.CharField(max_length=100, name="product_name")
    cost = models.IntegerField(name="cost")
    rating = models.IntegerField(name="rating")
    quantity = models.IntegerField(name="quantity", default=1)
    description = models.TextField(name="description", default="")
    seller = models.CharField(max_length=100, name="seller", default="sahara")
    product_pic = models.ImageField(default='item.png', upload_to="products", name="product_pic")

    def __str__(self):
        return self.product_name
