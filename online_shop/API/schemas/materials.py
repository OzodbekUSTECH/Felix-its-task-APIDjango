from ninja import ModelSchema, Schema, Field
from ..models import ProductMaterial

class ProductMaterialSchema(ModelSchema):
    price: int | None = Field(None, alias="warehouse.price")
    warehouse_id: int | None = Field(None, alias="warehouse.pk")
    material_name: str = Field(..., alias="material.name")

    class Meta:
        model = ProductMaterial
        fields = ["id", "qty"]