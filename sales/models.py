from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    subsidiary = models.ForeignKey('subsidiaries.Subsidiary', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(null=False, blank=False)
    
    def save(self, *args, **kwargs ):
        self.price = self.product.price
        return super().save( *args, **kwargs )

    def __str__(self):
        return f"{self.product.name} - {self.quantity} @ {self.price}"
    
