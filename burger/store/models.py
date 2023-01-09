from django.db import models
from django.urls import reverse


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    class Meta:
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store_category', kwargs={"slug": self.slug})


class Product(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    image = models.ImageField(upload_to='products_img', blank=True)
    description = models.TextField(blank=True)
    short_desription = models.CharField(max_length=64, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.name} | {self.category.name}'

    def get_absolute_url(self):
        return reverse('product', kwargs={"slug": self.slug})
