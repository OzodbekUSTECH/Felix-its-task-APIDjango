from ..schemas import products as p_schema
from ..unitOfWork import UnitOfWork


class ProductsService:
    """
    В services находится основная бизнес-логика приложения
    """

    def get_products(self, uow: UnitOfWork):
        with uow:
            return uow.products.get_all()