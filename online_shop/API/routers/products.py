from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate,
    PageNumberPaginationExtra,
    PaginatedResponseSchema,
)
from ..schemas import products as p_schema
from ..services.products import ProductsService
from ..unitOfWork import UnitOfWork

@api_controller("/products", tags=["Products"])
class ProductsController:
    """
    Все endpoints принадлежащие продуктам(товарам)
    """
    def __init__(self, products_service: ProductsService, uow: UnitOfWork):
        self.products_service = products_service
        self.uow = uow



    @route.get('/', response=PaginatedResponseSchema[p_schema.ProductSchema])
    @paginate(PageNumberPaginationExtra, page_size=50)
    def get_groups(self):
        return self.products_service.get_products(self.uow)