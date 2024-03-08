from django.db import models
from .materials import Material

class Warehouse(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name = "warehouses")
    qty = models.PositiveBigIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def reminder(self):
        """
        В warehouse когда приходит материла, его кол-во изначальное не меняем,
        вместо этого, мы берем все product_materials и оттуда вычесляем остаток
        """
        product_materials = self.product_materials.all()
        reminded_qty = self.qty
        for product_material in product_materials:
            reminded_qty -= product_material.qty
        return reminded_qty

    def __str__(self):
        return f"{self.material.name} - {self.qty} - {self.price} - Ост: {self.reminder}"