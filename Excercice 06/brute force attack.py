#asking user to enter password
Enter_Password=(int(input("enter the password:")))

#correct_password
correct_password=(12345)

#using while loop
while True:

    if Enter_Password==correct_password:
       print("correct password")
       break
    else:
       print("incorrect password try again")
       Enter_Password=(int(input("enter the password:")))