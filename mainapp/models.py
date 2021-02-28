from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    discription = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=128, unique=True)
    discription = models.TextField(blank=True)
    brief_discription = models.TextField(blank=True)
    prace = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    imege = models.ImageField(upload_to='products_imege', blank=True)
    cattegory = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} | {self.cattegory.name}'
