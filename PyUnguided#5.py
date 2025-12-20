#My second unguided project will be an advance log in system that asks for their username, password and their birthday when registering.
#When they input their birthday it will verify if they are above 18, if they are, they will be able to register.
#Additionally, they will also have an option to register. It will store the data until the very end. And add additional things inside when they are logged in.
class register:
     
    def username(self):
        self.user = input("Input the username you want: ")
        return self.user

    def password(self):
        self.pswrd = input("Input the password you want: ")
        return self.pswrd
    
class creds:
    
    def __init__(self):
        credentials = {'user': login.user, 'password': login.pswrd}

login = register()
creden = creds()
