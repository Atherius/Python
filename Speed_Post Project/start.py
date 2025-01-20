import User as usr
import delivery as dlv
import logger as lg
class prompt:
    '''This class is used to accept user choice for registration.'''
    def __init__(self):
        self.type = input("Are you a User or a Delivery Person? (U/D): ")
        print("{:=^50}".format("="))
        
    def get_choice(self):
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
            lg.Logger().log_error("Invalid Choice!")
            print("Invalid choice")
    
speedpost = prompt()
speedpost.get_choice()