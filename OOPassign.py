
class User: # Create the user class (blueprint)
    def __init__(self,name, email, address): # include the states to create instances of these states later for the individual user
        #instance attributes
        self.name = name
        self.email = email
        self.address  = address
        #instance method
    def display_user_info(self): #create a greeting for the user 
        print(f"Hello {self.name} ! Welcome to Los Pollos Hermanos Pizza! The information you have given is: Name: {self.name} Email: {self.email} Address: {self.address}")

    def __str__(self): #create a string for the personal detail summary
        return f'Thank you for your order {self.name}! Your pizza will be handmade and delivered to {self.address} and your receipt will be emailed to {self.email}. Thanks again for supporting Los Pollos Hermanos Pizza, where something delicious is always cooking!'

class Pizza: # create Pizza class (blueprint)
    def __init__(self,size, boxes: int, price: int): # include the states to create instances of these states later for the individual user
        #instance attributes
        self.size = size
        self.boxes = boxes
        self.price = price

        #instance method
        #Getters
    def get_small(self): # Get the initial price of one box of a small size pizza
        if self.size == "Small":
            self.price += 10
            return self.price

    def get_medium(self):
        if self.size == "Medium": # Get the initial price of one box of a medium size pizza
            self.price += 12
            return self.price
    def get_large(self):
        if self.size == "Large": # Get the initial price of one box of a large size pizza
            self.price += 15 # store it in self.price for further operations later on
            return self.price
    
        #Setters
    def set_price(self,value): # create operation that involves multiplying cost by the number of boxes to set cost without discount
        self.value = value 
        self.price = self.price * self.boxes
        print("Cost before promotions and discounts:")
        return self.price
        

    def set_price_discount(self, discount): # create operation that involves multiplying cost by the number of boxes and by 0.15 to set up cost with discount
        self.discount = discount
        if self.boxes >= 3: # If it is equal to or greater than 3, discount will be applied
            self.discount = (self.price) * 0.15
            self.price = self.price - self.discount
            print("Total with discount:")
            return self.price
        elif self.boxes < 3: # Display message when there is no disount
            print("Discount:")
        

        
        #string
    def __str__(self):
        return f'The best deal for {self.boxes} {self.size} pizza boxes, with the consideration of the 15% off your order when you order three or more pizzas deal going on is, ${self.price} CAD. ****So your final total is ${self.price} CAD.**** '
    
        


User_name = input("What is your name?")
User_email = input("What is your email?")
User_address = input("What is your address?")
User_info = User(User_name,User_email,User_address)
User_info.display_user_info()

User_size = input("What size pizza would you like: Small - $10 , Medium - $12 , or Large - $15? ")
User_box = float(input("How many pizzas would you like of this size? ***15% off when you buy 3 or more!***"))
User_order = Pizza(User_size, User_box, 0)

if User_size == "Small":
    User_order.get_small() 
    print(User_order.set_price(10))
    print(User_order.set_price_discount(10))
    print(User_order.__str__())
elif User_size == "Medium":
    User_order.get_medium() 
    print(User_order.set_price(12))
    print(User_order.set_price_discount(12))
    print(User_order.__str__())
elif User_size == "Large":
    User_order.get_large() 
    print(User_order.set_price(15))
    print(User_order.set_price_discount(15))
    print(User_order.__str__())

print(User_info.__str__())
