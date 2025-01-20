from logger import Logger

class Feedback:
    '''This class is used to accept feedback from users for delivery partners.'''
    def __init__(self):
        self.logger = Logger()
        self.delivery_partner_id = input("Enter Delivery Partner ID: ")
        self.rating = self.get_rating()
        self.review = input("Enter your review: ")
        self.logger.log_info(f"Feedback received for Delivery Partner ID: {self.delivery_partner_id}")

    def get_rating(self):
        '''Get a valid rating from the user.'''
        while True:
            try:
                rating = int(input("Enter rating (1-5): "))
                if 1 <= rating <= 5:
                    return rating
                else:
                    self.logger.log_warning("Invalid rating. Please enter a number between 1 and 5.")
                    print("Invalid rating. Please enter a number between 1 and 5.")
            except ValueError:
                self.logger.log_warning("Invalid input. Please enter a number between 1 and 5.")
                print("Invalid input. Please enter a number between 1 and 5.")

    def show_feedback(self):
        '''Display feedback details.'''
        print("{:=^50}".format(" Feedback Details "))
        print(f"Delivery Partner ID: {self.delivery_partner_id}")
        print(f"Rating: {self.rating}")
        print(f"Review: {self.review}")
        print("{:=^50}".format("="))

fbk = Feedback()
fbk.show_feedback() 