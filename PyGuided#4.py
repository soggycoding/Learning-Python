## First Project, a grocery list that will ask for your input for the things you need and will list them down after you finish writing it.
## it will ask what you'll input and will have a confirmation (y/n) to avoid mistakes or errors
## if possible, it should also ask for the last time if there will be any revisions to the list before giving the final print
product_list = []
while True:
    question = input("Would you like to add something in the list? (yes/no) ").lower()
   
    if question == "yes":
        product_name = input("Input the product you want to add to the list: ")
        confirmation = input(f"Are you sure that you want to add " + product_name.upper() + " to the list? (y/n)").lower()
        if confirmation == "y":
            product_list.append(product_name)
            print("Succesfully added to the list.")
        elif confirmation == "n":
            product_name = input("Input the correct product you want to add: ")
            product_list.append(product_name)
            
    elif question == "no":
        
        print(f"Here is the grocery list\n", product_list)
        break
    
    else:
        print("Input a valid answer")
        break