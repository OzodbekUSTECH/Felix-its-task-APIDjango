from typing import Type
from . import repositories
from . import models





class UnitOfWork:
    """
    Использовал Unit Of Work(UOW) для удобства работы с несколькими моделями в одном запросе, 
    но в FastAPI, я использовал его, чтобы еще управлять транзакциями.
    """
    products: Type[repositories.ProductsRepository]
    materials: Type[repositories.MaterialsRepository]
    warehouses: Type[repositories.WarehousesRepository]
    product_materials: Type[repositories.ProductMaterialsRepository]

    def __enter__(self):
        self.products = repositories.ProductsRepository(model=models.Product)
        self.materials = repositories.MaterialsRepository(model=models.Material)
        self.warehouses = repositories.WarehousesRepository(model=models.Warehouse)
        self.product_materials = repositories.ProductMaterialsRepository(model=models.ProductMaterial)

    def __exit__(self, *args):
        return
    
    