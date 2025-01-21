import User as usr
import delivery as dlv
import logging
import sys

import conssignment as cons
logging.basicConfig(
    filename='application.log',  
    level=logging.DEBUG,  
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  
)
class prompt:
    '''This class is used to accept user choice for registration.'''
    def __init__(self):
        try:
            self.type = input("Are you a User or a Delivery Person? (U/D): ").upper()
            if self.type not in ['U','D']:
                raise ValueError("Invalid Input add U for user and D for Delivery Boy")
            print("{:=^50}".format("="))
        except Exception :
             print(f"Unexpected error: {sys.exc_info()[0]}")

    def get_choice(self):
        '''  Processes the user's choice based on their input
             This method checks the type of user input ('U' for User or 'D' for Delivery Person).
             It creates the respective objects and validates them 

            Raises:
                RuntimeError: If the input type is invalid or the object initialization fails.
                AttributeError: If the required methods or attributes are missing in the imported modules.
                ValueError: If the user type is invalid.
                Exception: For any unexpected errors during execution.
          
              '''
        try:
            var = self.type.capitalize()
            if var == 'U':
                self.obj = usr.user()
                self.obj.validate_user()
                return self.obj.show_user()
            elif var == 'D':
                self.obj = dlv.delivery()
                self.obj.validate_user()
                return self.obj.show_user()
            else:
               raise ValueError("Unexpected error occurred with user type selection.")
               

        except AttributeError as e:
            logging.error(f"Attribute Error: {e}")
            print("An error occurred during object initialization or method execution.")
        except ValueError as e:
            logging.error(f"Value Error: {e}")
            print(e)
        except Exception as e:
            logging.error(f"Unexpected Error: {e}")
            print("An unexpected error occurred. Please try again.")
    
speedpost = prompt()
speedpost.get_choice()

while True:
            print("\nUser Options:")
            print("1. Add a new consignment")
            print("2. Track an existing consignment")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                consignment = cons.Consignment()
                consignment.show_consignment_details()
            elif choice == '2':
                tracking_id = input("Enter the tracking ID to track: ")
                logging.info(f"Tracking consignment with ID: {tracking_id}")
                print(f"Tracking details for {tracking_id} (Functionality to be implemented).")
            elif choice == '3':
                print("Exiting User Menu...")
                break
            else:
                print("Invalid choice. Please try again.")