import re
import validationerr as ve
import logger

class user:
    '''This class is used to accept user details for registration.'''
    def __init__(self):
        self.log=logger.Logger()
        self.fname = input("Enter your first name: ")
        self.lname = input("Enter your last name: ")
        self.email = input("Enter your email: ")
        self.phone = input("Enter your phone number: ")
        self.address = input("Enter your address: ")
        self.pincode = input("Enter your zipcode: ")
        self.pin = input("Enter your pin: ")

    def validate_user(self):
        '''validating user using decorator'''
        def validate_user(pattern):
            def decorator(func):
                def wrapper(value):
                    if re.match(pattern, value):
                        return func(value)
                    else:
                        self.log.log_error("Validation Failed!")
                        raise ve.ValidationERR("Invalid Input Format!")
                return wrapper
            return decorator

        @validate_user("^[A-Za-z]+$")
        def fname_validate(fname):
            self.log.log_info("User Validation")
            self.log.log_info("FirstName Validation Successful!")
            print(f"First Name is {fname}")

        @validate_user("^[A-Za-z]+$")
        def lname_validate(lname):
            self.log.log_info("LastName Validation Successful!")
            print(f"Last Name is {lname}")

        @validate_user("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        def email_validate(email):
            self.log.log_info("Email Validation Successful!")
            print(f"Email ID is {email}")

        @validate_user("^[0-9]{10}$")
        def phone_validate(phone):
            self.log.log_info("Mobile Number Validation Successful!")
            print(f"Mobile Number is {phone}")

        @validate_user("^[A-Za-z0-9]+$")
        def address_validate(address):
            self.log.log_info("Address Validation Successful!")
            print(f"The Address is {address}")

        @validate_user("^[0-9]{5}$")
        def pincode_validate(pincode):
            self.log.log_info("Zipcode Validation Successful!")
            print(f"Your Zip Code is {pincode}")

        @validate_user("^[0-9]{5}$")
        def pin_validate(pin):
            self.log.log_info("Pin Validation Successful!")
            print(f"Pin is {pin}")

        self.fname_validate = fname_validate
        self.lname_validate = lname_validate
        self.email_validate = email_validate
        self.phone_validate = phone_validate
        self.address_validate = address_validate
        self.pincode_validate = pincode_validate
        self.pin_validate = pin_validate

    def show_user(self):
        '''returning user details'''
        print("{:=^50}".format(" User Details "))
        self.fname_validate(self.fname)
        self.lname_validate(self.lname)
        self.email_validate(self.email)
        self.phone_validate(self.phone)
        self.address_validate(self.address)
        self.pincode_validate(self.pincode)
        self.pin_validate(self.pin)
        print("{:=^50}".format("="))