## First Project, a grocery list that will ask for your input for the things you need and will list them down after you finish writing it.
## it will ask what you'll input and will have a confirmation (y/n) to avoid mistakes or errors
## if possible, it should also ask for the last time if there will be any revisions to the list before giving the final print
class add_cart:
    def __init__(self):
        self.add = []
    def get_product(self):
        self.product_name = input("Input the product you want to add to the list: ").upper()
        return self.product_name
    def confirm(self):
        self.confirmed = cart.add.insert(1, product)
        print("Succesfully ", product ," added to the list.")
        
cart = add_cart()

while True:
    question = input("Would you like to add something in the list? (y/n) ").lower()
   
    if question == "y":
        product = cart.get_product()
        confirmation = input("Are you sure that you want to add " + product + " to the list? (y/n)")
        if confirmation == "y":
            final = cart.confirm()
        elif confirmation == "n":
            cart.get_product()
            cart.confirm()
            
    elif question == "n":
        
        print("Here is the grocery list\n", cart.add)
        revise = input("Would you like to remove something from the list? (y/n) ")
        if revise == "y":
            while True:
                remove = input("What would you like to remove from the list? Input ""NONE"" if there isnt any. ").upper()
                if remove in cart.add:
                    cart.add.remove(remove)
                    print("Here is what remains in the list", cart.add)
                    
                elif remove == "NONE":
                    print("Here is the final grocery list ", cart.add)
                    break
                break
        elif revise == "n":
            print("Here is the final grocery list ", cart.add)
            break
        break
            
    else:
        print("Input a valid answer")
        break
