# the loop
while True:
    # asking user for choose the topping
    topping = input("choose the pizza topping (or write 'quit' to stop it): ")
    
    # stopping the loop 
    if topping == 'quit':
        break
    
    # print message 
    print("you added " + topping + " to your pizza!")
