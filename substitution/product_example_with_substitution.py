class Product:

    PERCENTAGE_DISCOUNT = 10

    def get_discount(self):
        return self.PERCENTAGE_DISCOUNT


class InHouseProduct(Product):

    def apply_extra_discount(self):
        self.PERCENTAGE_DISCOUNT += 0.5

    def apply_extra_discount_buying_with_bitcoin(self):
        self.PERCENTAGE_DISCOUNT += 2

    def get_discount(self):
        """
        get_discount can be substituted by their subtypes without affecting the
        correctness of the program.
        Here is where the Liskov Substitution Principle is applied.
        The solution to this pattern is called 'Tell, Don't Ask'
        """
        self.apply_extra_discount()
        self.apply_extra_discount_buying_with_bitcoin()
        return self.PERCENTAGE_DISCOUNT


class InCommerceDiscount(Product):

    def apply_extra_discount(self):
        self.PERCENTAGE_DISCOUNT += 1

    def get_discount(self):
        """
        get_discount can be substituted by their subtypes without affecting the
        correctness of the program.
        Here is where the Liskov Substitution Principle is applied.
        The solution to this pattern is called 'Tell, Don't Ask'
        """
        self.apply_extra_discount()
        return self.PERCENTAGE_DISCOUNT


def client():
    """
    The client does not need to ask anything. This is what we mean by 'Tell, Don't Ask'
    """
    products_lists = [InCommerceDiscount(), InHouseProduct()]

    for pro in products_lists:
        print(pro.get_discount())


if __name__ == '__main__':
    client()
