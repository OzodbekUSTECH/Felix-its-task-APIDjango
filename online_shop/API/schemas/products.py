from ninja import ModelSchema, Schema
from ..models import Product
from .materials import ProductMaterialSchema

class ProductSchema(ModelSchema):
    product_materials: list[ProductMaterialSchema]
    class Meta:
        model = Product
        fields = "__all__"