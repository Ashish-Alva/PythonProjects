from django.db import models

# Create your models here.
class Customer(models.Model):
    FirstName = models.CharField(max_length=50, null=True)
    LastName  = models.CharField(max_length=50, null=True)
    Email = models.EmailField(max_length=100, null=True)
    CreatedAt = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"