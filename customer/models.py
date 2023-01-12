from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.customer_name