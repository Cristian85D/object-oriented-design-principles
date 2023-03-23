"""
Inversion of control(IOC) in Java:
It is closely related, so we'll cover it quickly.

The ProductCatalog had a constructor which took in a ProductRepository object.
The class that calls the ProductCatalog will provide or 'inject' the object.

But even though the injection happens outside of ProductCatalog, the injection
still happens during the main control flow of the program. i.e. injection is
happening in the main thread of program execution.

What if we want all the injections to happen in a separate thread or a
separate context altogether,
so that the main control flow is kept completely isolated from injection?
This can be achieved using frameworks.
If your preferred programming language is Java, then the Spring Framework is
a popular choice.

Spring will run in its own context,
different from the main flow of control of the program.
Spring will take care of injecting the required dependencies of a class.
So if you want to instantiate an object of a class, instead of doing it yourself directly in the
code, you ask Spring to give you an object of the class.

The Spring Framework first looks at all the dependencies required for the object instantiation,
then goes ahead and injects each dependency and instantiates the object,
and gives it back to the main control flow.

Thus the control over dependency injection is completely delegated to the Spring
Framework and does not happen in the main control flow.
This concept is called inversion of control.
And Spring is called an inversion of control container or simply an
IOC container.

Inversion of control in Python:
https://stackoverflow.com/questions/2461702/why-is-ioc-di-not-common-in-python
"""

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

