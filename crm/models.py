from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category = models.CharField(max_length=10, choices=[('crm', 'CRM'), ('erp', 'ERP'), ('wms', 'WMS')])

    def __str__(self):
        return f"{self.name} ({self.category})"
