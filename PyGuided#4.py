## First Project, a grocery list that will ask for your input for the things you need and will list them down after you finish writing it.
## it will ask what you'll input and will have a confirmation (y/n) to avoid mistakes or errors
## if possible, it should also ask for the last time if there will be any revisions to the list before giving the final print
added = []
class add_cart:
    def __init__(self):
        self.product_name = input("Input the product you want to add to the list: ").upper()
        

while True:
    question = input("Would you like to add something in the list? (y/n) ").lower()
   
    if question == "y":
        product = add_cart()
        confirmation = input("Are you sure that you want to add " + product.product_name + " to the list? (y/n)")
        if confirmation == "yes":
            added.insert(product.product_name)
            print("Succesfully added", product.product_name, "to the list.")
        elif confirmation == "no":
            product_name = input("Input the correct product you want to add: ")
            
    elif question == "n":
        
        print("Here is the grocery list\n", added)
        break
    
    else:
        print("Input a valid answer")
        break
