from abc import ABC, abstractmethod

class ProductRepository(ABC): # this is the abstraction

    @abstractmethod
    def get_all_product_names(self):
        pass


class SQLProductRepository(ProductRepository):  # low level class

    def get_all_product_names(self):
        return ['jean', 'shirt']


class ProductFactory:

    @staticmethod
    def create_sql_product_repository():
        return SQLProductRepository()


class ProductCatalog:  # high level class

    def __init__(self, product_repository:SQLProductRepository):
        """
        We don't want the ProductCatalog to worry about how and when to
        trigger the instantiation of SQLProductRepository.
        ProductCatalog does NOT need to worry about any instantiation.
        We are injecting the dependency INTO ProductCatalog , instead of
        ProductCatalog worrying about instantiating the dependency.
        This is the concept of dependency injection.
        """
        self.product_repository = product_repository

    def list_all_products(self):
        all_product_names = self.product_repository.get_all_product_names()
        print(f'All products names: {all_product_names}')


def ecommerce_main_application():
    """
    This method inject the dependency sql_product_repository in ProductCatalog
    """
    sql_product_repository = ProductFactory.create_sql_product_repository()
    product_catalog = ProductCatalog(product_repository=sql_product_repository)  # We are injecting the dependency INTO ProductCatalog , instead of ProductCatalog worrying about instantiating the dependency. This is the concept of dependency injection.
    product_catalog.list_all_products()


if __name__ == '__main__':
    ecommerce_main_application()
