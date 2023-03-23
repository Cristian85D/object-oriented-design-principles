class Product:

    PERCENTAGE_DISCOUNT = 10

    def get_discount(self):
        return self.PERCENTAGE_DISCOUNT


class InHouseProduct(Product):

    def apply_extra_discount(self):
        self.PERCENTAGE_DISCOUNT += 0.5

    def apply_extra_discount_buying_with_bitcoin(self):
        self.PERCENTAGE_DISCOUNT += 2


class InCommerceDiscount(Product):

    def apply_extra_discount(self):
        self.PERCENTAGE_DISCOUNT += 1


def client():
    """
    Client does need to ask if each pro isinstance from the specific class
    """
    products_lists = [InCommerceDiscount(), InHouseProduct()]

    for pro in products_lists:
        if isinstance(pro, InHouseProduct):  # we are asking or enquiring about the subtype
            pro.apply_extra_discount()
            pro.apply_extra_discount_buying_with_bitcoin()
        if isinstance(pro, InCommerceDiscount):
            pro.apply_extra_discount()

        print(pro.get_discount())

"""
Is NOT a good design. This is against the Liskov Substitution Principle.
We should have been able to deal with all the objects as Product objects itself 
instead of call isinstance() method to apply each discount for each product.
"""

if __name__ == '__main__':
    client()


