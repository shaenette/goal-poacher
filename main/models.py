import uuid
from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=50)
    is_featured = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
    @property
    def is_out_of_stock(self):
        return self.stock <= 0

    def decrease_stock(self, amount=1):
        if self.stock >= amount:
            self.stock -= amount
            self.save()
            return True
        return False

class Employee(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    persona = models.TextField()