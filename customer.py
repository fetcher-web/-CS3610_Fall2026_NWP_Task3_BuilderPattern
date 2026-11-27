class Customer:

    def __init__(self):
        self.firstName = None
        self.middleName = None
        self.lastName = None
        self.primaryEmail = None
        self.secondaryEmail = None
        self.primaryMobileNumber = None
        self.secondaryMobileNumber = None

    def __str__(self):
        return(
            f"First Name: {self.firstName}\n"
            f"Middle Name: {self.middleName}\n"
            f"Last Name: {self.lastName}\n"
            f"Primary Email: {self.primaryEmail}\n"
            f"Secondary Email: {self.secondaryEmail}\n"
            f"Primary Mobile Number: {self.primaryMobileNumber}\n"
            f"Secondary Mobile Number: {self.secondaryMobileNumber}"
        )
        return f"Customer Name: {self.name}, Email: {self.email}"