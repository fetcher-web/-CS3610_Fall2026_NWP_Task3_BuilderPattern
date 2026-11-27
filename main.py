from director import Director
from web_app_builder import WebAppBuilder
from mobile_app_builder import MobileAppBuilder

def main():

    director = Director()

    customerData = {
        "firstName": "John",
        "middleName": "Michael",
        "lastName": "Smith",
        "primaryEmail": "john.smith@example.com",
        "secondaryEmail": "john.smith2@example.com",
        "primaryMobileNumber": "123-456-7890",
        "secondaryMobileNumber": "234-567-8901",
    }

    # Web application customer
    webBuilder = WebAppBuilder()
    director.builder = webBuilder

    director.make(customerData)

    webCustomer = webBuilder.product
    
    print("---Web Application Customer ---")
    print(webCustomer)

    # Mobile application customer
    mobileBuilder = MobileAppBuilder()
    director.builder = mobileBuilder

    director.make(customerData)

    mobileCustomer = mobileBuilder.product

    print("---Mobile Application Customer ---")
    print(mobileCustomer)

if __name__ == "__main__":
    main()