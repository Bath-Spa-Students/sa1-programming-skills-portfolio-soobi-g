def check_even_odd(number):
    if number % 2 == 0:  
        return "Number is even"
    else:
        return "number is odd"
# 
def main():
# input the number
    number = int(input("enter number: "))  

    #checking number 
    conclusion = check_even_odd(number)
    
    #get result
    print("The number is", conclusion)
# 
main()  
