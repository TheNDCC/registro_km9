from django.db import models

# Create your models here.
class Expense(models.Model):
    subsidiary = models.ForeignKey('subsidiaries.Subsidiary', on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(null=False, blank=False)

    def __str__(self):
        return f"{self.description} - {self.amount}"

class Credit(models.Model):
    subsidiary = models.ForeignKey('subsidiaries.Subsidiary', on_delete=models.CASCADE)
    employee = models.ForeignKey('employees.Employee', on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(null=False, blank=False)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.description or self.employee} - {self.amount}"
    
class Payment(models.Model):
    subsidiary = models.ForeignKey('subsidiaries.Subsidiary', on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(null=False, blank=False)

    def __str__(self):
        return f"{self.description} - {self.amount}"
    