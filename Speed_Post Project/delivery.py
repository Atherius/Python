import re
import validationerr as ve
import logger

class delivery:
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
        self.liscence = input("Enter your liscence number: ")
        self.aadhar= input("Enter your aadhar number: ")
        self.pan= input("Enter your pan number: ")

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
            self.log.log_info("Delivery Partner Validation")
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
            
        @validate_user("^[0-9]{12}$")
        def liscence_validate(liscence):
            self.log.log_info("Driving Liscence Validation Successful!")
            print(f"Liscence Number is {liscence}")
        
        @validate_user("^[0-9]{12}$")
        def aadhar_validate(aadhar):
            self.log.log_info("Aadhar Validation Successful!")
            print(f"Aadhar Number is {aadhar}")
            
        @validate_user("^[A-Z]{5}[0-9]{4}[A-Z]{1}$")
        def pan_validate(pan):
            self.log.log_info("Pan Card Validation Successful!")
            print(f"Pan Number is {pan}")

        self.fname_validate = fname_validate
        self.lname_validate = lname_validate
        self.email_validate = email_validate
        self.phone_validate = phone_validate
        self.address_validate = address_validate
        self.pincode_validate = pincode_validate
        self.pin_validate = pin_validate
        self.liscence_validate = liscence_validate
        self.aadhar_validate = aadhar_validate
        self.pan_validate = pan_validate

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
        self.liscence_validate(self.liscence)
        self.aadhar_validate(self.aadhar)
        self.pan_validate(self.pan)
        print("{:=^50}".format("="))