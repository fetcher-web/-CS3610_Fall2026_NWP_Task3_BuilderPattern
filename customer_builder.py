from abc import ABC, abstractmethod
from customer import Customer

class CustomerBuilder(ABC):

    @property
    @abstractmethod
    def product(self) -> Customer:
        pass    

    @abstractmethod
    def firstName(self, value: str) -> "CustomerBuilder":
        pass

    @abstractmethod
    def middleName(self, value: str) -> "CustomerBuilder":
        pass   

    @abstractmethod
    def lastName(self, value: str) -> "CustomerBuilder":
        pass    

    @abstractmethod
    def primaryEmail(self, value: str) -> "CustomerBuilder":    
        pass

    @abstractmethod
    def secondaryEmail(self, value: str) -> "CustomerBuilder":
        pass

    @abstractmethod
    def primaryMobileNumber(self, value: str) -> "CustomerBuilder":
        pass

    @abstractmethod
    def secondaryMobileNumber(self, value: str) -> "CustomerBuilder":
        pass

    