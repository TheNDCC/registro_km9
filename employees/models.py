from django.db import models

# Create your models here.
class Employee(models.Model):
    subsidiary = models.ForeignKey('subsidiaries.Subsidiary', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.full_name} - {self.position}"

class Commission(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    subsidiary = models.ForeignKey('subsidiaries.Subsidiary', on_delete=models.CASCADE)
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2)
    sale_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    total_commission = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('date', 'employee')

    def __str__(self):
        return f"{self.employee.full_name} - {self.date}"