#My second unguided project will be an advance log in system that asks for their username, password and their birthday when registering.
#When they input their birthday it will verify if they are above 18, if they are, they will be able to register.
#Additionally, they will also have an option to register. It will store the data until the very end. And add additional things inside when they are logged in.
new = input("Are you new here? ") #asked if the user is new

class register:
    def reg(self):
        self.new_user = input("Please input the username you want: ")
        return self.new_user
    def pswrd(self):
        self.new_pass = input("Please input the password you want: ")
        while self.confirmation != self.new_pass:
            self.confirmation()
            if self.confirmation == self.new_pass:
                print("Password confirmed, please log in again.")
                return self.new_pass
                break
                
            else:
                print("You have input the wrong password.")
    def confirmation(self):
        self.confirm_pass = input("Please confirm your password, input it again: ")
        
        

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
