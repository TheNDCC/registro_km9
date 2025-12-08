from django.db import models

# Create your models here.
class Subsidiary(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name
class CashFlow(models.Model):
    date = models.DateField()
    cash = models.DecimalField(max_digits=10, decimal_places=2)
    card = models.DecimalField(max_digits=10, decimal_places=2)
    diff = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    subsidiary = models.ForeignKey(Subsidiary, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} - {self.description} - {self.amount}"