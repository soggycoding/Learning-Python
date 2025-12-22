#My second unguided project will be an advance log in system that asks for their username, password and their birthday when registering.
#When they input their birthday it will verify if they are above 18, if they are, they will be able to register.
#Additionally, they will also have an option to register. It will store the data until the very end. And add additional things inside when they are logged in.
new = input("Are you new here? ") #asked if the user is new
if new == "yes": #if yes they will register
    new_user = input("Please input the username you want: ")
    print(f"Okay ", new_user ," is available")
    new_pass = input("Please input the password you want: ")
    confirm_pass = input("Please input the password again just to make sure: ")
    if new_pass == confirm_pass:
        print("The password is confirmed, account is created.") #After register, they should be asked to log in again as a user. From there they should be able to do anything inside the app
        
    else:
        print("Wrong password, try again tomorrow")
elif new == "no":
    user = input("Please input your username: ")
    print(f"Welcome back!", user)
    password = input("Please input your password: ")
    print("Log in confirmed")
    
else: 
    print("Wrong input, try again.")
