import logging


logging.basicConfig(
    filename='application.log',  
    level=logging.DEBUG,         
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  
)

class Feedback:
    '''This class is used to accept feedback from users for delivery partners.'''
    def __init__(self):
        
        self.delivery_partner_id = input("Enter Delivery Partner ID: ")
        self.rating = self.get_rating()
        self.review = input("Enter your review: ")
        logging.info(f"Feedback received for Delivery Partner ID: {self.delivery_partner_id}")

    def get_rating(self):
        '''Get a valid rating from the user.'''
        while True:
            try:
                rating = int(input("Enter rating (1-5): "))
                if 1 <= rating <= 5:
                    return rating
                else:
                    logging.warning("Invalid rating. Please enter a number between 1 and 5.")
                    print("Invalid rating. Please enter a number between 1 and 5.")
            except ValueError:
                logging.warning("Invalid input. Please enter a number between 1 and 5.")
                print("Invalid input. Please enter a number between 1 and 5.")

    def show_feedback(self):
        '''Display feedback details.'''
        try:
            print("{:=^50}".format(" Feedback Details "))
            print(f"Delivery Partner ID: {self.delivery_partner_id}")
            print(f"Rating: {self.rating}")
            print(f"Review: {self.review}")
            print("{:=^50}".format("="))
        except Exception as e:
            logging.error(f"Error displaying feedback: {e}")
            print("An unexpected error occurred while displaying feedback. Please try again")


fbk = Feedback()
fbk.show_feedback() 