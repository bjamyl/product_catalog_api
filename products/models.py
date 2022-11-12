from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='product_images/%Y/%m/%d/', blank=True)
    def __str__(self):
        return self.name