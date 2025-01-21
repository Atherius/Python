import random
import string
import logging

logging.basicConfig(
    filename='application.log',  
    level=logging.DEBUG,  
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log format with timestamp, name, level, and message
)
class Consignment:
    '''This class is used to generate consignment tracking ID based on user consignment type and address'''
    def __init__(self):
        try:
            
            self.consignment_type = input("Enter consignment type (e.g., Document, Parcel): ")
            self.pickup_address = input("Enter pickup address: ")
            self.pickup_pincode = input("Enter pickup pincode: ")
            self.delivery_address = input("Enter delivery address: ")
            self.delivery_pincode = input("Enter delivery pincode: ")
            self.tracking_id = self.generate_tracking_id()
            logging.info(f"Consignment created with Tracking ID: {self.tracking_id}")
            print(f"Consignment created successfully with Tracking ID: {self.tracking_id}")
        except Exception as e:
            logging.error(f"Error during consignment creation: {e}")
            print("An unexpected error occurred. Please try again")

    def generate_tracking_id(self):
        '''Generate a unique tracking ID for the consignment.'''
        try:
            prefix = ''.join(random.choices(string.ascii_uppercase, k=3))
            suffix = ''.join(random.choices(string.digits, k=7))
            return f"{prefix}{suffix}"
        except Exception as e:
            logging.error(f"Error generating tracking ID: {e}")
            raise RuntimeError("Failed to generate tracking ID") from e

    def show_consignment_details(self):
        '''Display consignment details.'''
        try:
            print("{:=^50}".format(" Consignment Details "))
            print(f"Consignment Type: {self.consignment_type}")
            print(f"Pickup Address: {self.pickup_address}")
            print(f"Pickup Pincode: {self.pickup_pincode}")
            print(f"Delivery Address: {self.delivery_address}")
            print(f"Delivery Pincode: {self.delivery_pincode}")
            print(f"Tracking ID: {self.tracking_id}")
            print("{:=^50}".format("="))
        except Exception as e:
            logging.error(f"Error displaying consignment details: {e}")
            print("An error occurred while displaying consignment details.")

obj=Consignment()
obj.show_consignment_details()