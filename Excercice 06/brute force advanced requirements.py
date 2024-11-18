#asking user to enter password
Enter_Password=(int(input("enter the password:")))

#correct_password
correct_password=(12345)

#using while loop
while True:

    if Enter_Password==correct_password:
       print("correct password")
     
    else:
       print("incorrect password try again 4 attempts remaining")
       Enter_Password=(int(input("enter the password:")))

       print("incorrect password try again 3 attempt ramining")
       Enter_Password=(int(input("enter the password:")))

       print("incorrect password try again 2 attempt ramining")
       Enter_Password=(int(input("enter the password:")))

       print("incorrect password try again 1 attempt ramining")
       Enter_Password=(int(input("enter the password:")))
       print("incorrect password try again 0 attempt ramining we ve alerted the authorities")
       Enter_Password=(int(input("enter the password:")))
    break
