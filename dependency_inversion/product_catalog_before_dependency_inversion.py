"""
So ProductCatalog directly depends on SQLProductRepository, so this is the
violation of the principle as seen in code.

So the definition gives us some guidance on how to fix this violation as well:
Both should depend on abstractions.
"""

class SQLProductRepository:  # low level module

    def get_all_product_names(self):
        return ['jean', 'shirt']


class ProductCatalog: # high level module

    def list_all_products(self):
        sql_repository = SQLProductRepository()  # We have tight coupling with SQLProductRepository
        all_product_names = sql_repository.get_all_product_names()
        print(f'All products names: {all_product_names}')


if __name__ == '__main__':
    ProductCatalog().list_all_products()
