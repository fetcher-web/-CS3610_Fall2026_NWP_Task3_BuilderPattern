from customer import Customer
from customer_builder import CustomerBuilder

class MobileAppBuilder(CustomerBuilder):

    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._product = Customer()

    @property
    def product(self) -> Customer:
        currentProduct = self._product
        self.reset()
        return currentProduct

    def firstName(self, value: str) -> CustomerBuilder:
        self._product.firstName = value
        return self 

    def middleName(self, value: str) -> CustomerBuilder:
        return self

    def lastName(self, value: str) -> CustomerBuilder:
        self._product.lastName = value
        return self

    def primaryEmail(self, value: str) -> CustomerBuilder:
        self._product.primaryEmail = value
        return self

    def secondaryEmail(self, value: str) -> CustomerBuilder:
        return self

    def primaryMobileNumber(self, value: str) -> CustomerBuilder:
        self._product.primaryMobileNumber = value
        return self

    def secondaryMobileNumber(self, value: str) -> CustomerBuilder:
        return self

    