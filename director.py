from customer_builder import CustomerBuilder

class Director:

    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> CustomerBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: CustomerBuilder) -> None:
        self._builder = builder 

    def make(self, customerData: dict) -> None:

        if self.builder is None:
            raise ValueError("No builder has been set for the director.")

        mandatoryFields =(
            "firstName",
            "lastName",
            "primaryEmail",
            "primaryMobileNumber"
        )

        for field in mandatoryFields:
            if not customerData.get(field):
                raise ValueError(f"Missing mandatory field: {field}")

        self.builder.firstName(customerData["firstName"])
        self.builder.middleName(customerData.get("middleName"))
        self.builder.lastName(customerData["lastName"])
        self.builder.primaryEmail(customerData["primaryEmail"])
        self.builder.secondaryEmail(customerData.get("secondaryEmail"))
        self.builder.primaryMobileNumber(customerData["primaryMobileNumber"])
        self.builder.secondaryMobileNumber(customerData.get("secondaryMobileNumber"))

        