from abc import ABC, abstractmethod


"""
ProductCatalog(high level module) --> ProductRepository(abstraction) <-- SQLProductRepository(low level module)

We are no longer violating the principle.
The high level module does not depend on the low level module anymore.
Both our high level and low level modules depend on the abstraction now.
"""

class ProductRepository(ABC): # this is the abstraction

    @abstractmethod
    def get_all_product_names(self):
        """
        Abstractions should not depend on details. Details should depend on abstractions.
        """
        pass


class SQLProductRepository(ProductRepository):  # low level class
    """
    The detail, which is the SQLProductRepository class,
    is dependent on the abstraction, which is the ProductRepository class.
    This is strictly as per the definition. -> "Abstractions should not depend on details. Details should depend on abstractions."
    """

    def get_all_product_names(self):
        """
        Los detalles(el codigo del metodo) dependen de implementar el metodo
        definido en la abstraccion(intertface ProductRepository).
        Tenemos que impementar detalles definidos en una abstraccion.
        """
        return ['jean', 'shirt']


class ProductFactory:

    @staticmethod
    def create_sql_product_repository():
        return SQLProductRepository()


class ProductCatalog:  # high level class
    """
    Our reference object is ProductRepository, so we don't have any
    tight coupling with SQLProductRepository anywhere in the
    ProductCatalog class.
    """

    def list_all_products(self):
        sql_product_repository = ProductFactory.create_sql_product_repository()  # Our reference is ProductRepository, so we don't have any tight coupling with SQLProductRepository
        all_product_names = sql_product_repository.get_all_product_names()

        print(f'All products names: {all_product_names}')


if __name__ == '__main__':
    ProductCatalog().list_all_products()
