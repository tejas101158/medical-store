from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = (
        ('rental', 'Rental'),
        ('surgical', 'Surgical'),
    )

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name