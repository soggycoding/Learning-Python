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
    def age_verification(self):
        from datetime import datetime
        self.birthdate  = input("Please input your birthdate using the following format MM/DD/YY: ")
        self.date1 = datetime.strptime(self.birthdate, '%m/%d/%y')
        self.date2 = datetime.now()
        self.age_by_days = (self.date2 - self.date1).days
        self.age = int(self.age_by_days / 365.25)
        if self.age < 18:
            print("You are currently under 18 and shall not progress further on the registration, thank you!")
            
        elif self.age >= 18:
            print(f"Age confirmed ", self.age ,",please proceed.")
            log_in.user_login()
    def email(self):
        self.user_email = input("Please input an email you can access: ")
        print("Email confirmed, please log in again.")
        
    def confirmation(self):
        self.confirm_pass = input("Please confirm your password, input it again: ")
        self.validate_input()
    def validate_input(self, max_tries=3):
        if self.confirm_pass == self.new_pass:
            print("Password confirmed, please provide your birthdate.")
            self.age_verification()
            return self.new_pass  
        while self.confirm_pass != self.new_pass:             
                self.confirm_pass = input("Incorrect input, please try again: ")
                self.tries += 1          
                if self.tries >= max_tries:
                    print("You have reached the max attempt of tries, please try again tomorrow ")
                    break

            
class cred():
    def credential(self, reg_instance):
        reg_instance = register()
        self.user = reg_instance.reg()
        self.user_pass = reg_instance.pswrd()
        self.user_age = reg_instance.age_verification()
        self.user_email = reg_instance.email()
        self.creds = {'user': self.user, 'password': self.user_pass, 'age': self.user_age, 'email': self.user_email}
        
class login():
    def user_login(self):
        self.log = input("Please input your username: ")
        authenticate.valid()
    def user_pass(self):
        self.login_pass = input("Please input your password:")

        
class authenticate():
    def auth(self, authentication):
        self.authentication = authentication
    
    def valid(self, username, password, creds_dict):
        self.username = log_in.user_login()
        self.password = log_in.user_pass()
        self.creds_dict = credentials.credential()
        if username == creds_dict['user']:
            print(f"{username}, exists. You may proceed")
            if password == creds_dict['password']:
                print("Password confirmed, welcome! ")
            
            
        
usercred = authenticate()
credentials = cred()
log_in = login()
user = register()
        
if new == "yes": #if yes they will register
    username = user.reg()
    password = user.pswrd()
    
else: 
    print("Wrong input, try again.")
    
