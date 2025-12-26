#My second unguided project will be an advance log in system that asks for their username, password and their birthday when registering.
#When they input their birthday it will verify if they are above 18, if they are, they will be able to register.
#Additionally, they will also have an option to register. It will store the data until the very end. And add additional things inside when they are logged in.
new = input("Please type 'yes' to register ") #asked if the user is new

class register:
    def reg(self):
        self.new_user = input("Please input the username you want: ")
        return self.new_user
    def pswrd(self):
        self.new_pass = input("Please input the password you want: ")
        self.tries = 0
        self.confirmation()
    def confirmation(self):
        self.confirm_pass = input("Please confirm your password, input it again: ")
        self.validate_input()
    def validate_input(self, max_tries=3):
        while self.confirm_pass != self.new_pass:             
                self.confirm_pass = input("Incorrect input, please try again: ")
                self.tries += 1
                if self.confirm_pass == self.new_pass:
                    print("Password confirmed, please log in again.")
                    return self.new_pass              
                if self.tries >= max_tries:
                    print("You have reached the max attempt of tries, please try again tomorrow ")
                    break

            
class cred():
    def credential(self, reg_instance):
        reg_instance = register()
        self.user = reg_instance.reg()
        self.userpass = reg_instance.pswrd()
        self.creds = {'user': self.user, 'password': self.userpass}
        
user = register()
        
if new == "yes": #if yes they will register
    username = user.reg()
    password = user.pswrd()
    
else: 
    print("Wrong input, try again.")
