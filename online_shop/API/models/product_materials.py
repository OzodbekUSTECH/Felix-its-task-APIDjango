from django.db import models
from django.core.exceptions import ValidationError
from .warehouses import Warehouse
from .materials import Material
from .products import Product

class ProductMaterial(models.Model):
    """
    Связь между продуктом, материалом и партий(складом(warehouse))
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_materials')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='product_materials')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name = "product_materials", null=True, blank=True)
    qty = models.PositiveIntegerField()

    
    
        
    def __str__(self):
        return f"{self.product.name} - {self.material.name} - {self.qty}"

    def clean(self):
        """
        Переопределяем метод сохранения в админке,
        делаем так, чтобы нельзя было сохранить если qty больше остатка в вебранном warehouse
        """
        super().clean()
        if self.warehouse:
            reminded_qty = self.warehouse.reminder
            if self.qty > reminded_qty:
                raise ValidationError({'qty': 'Количество не может быть больше остатка на складе'})