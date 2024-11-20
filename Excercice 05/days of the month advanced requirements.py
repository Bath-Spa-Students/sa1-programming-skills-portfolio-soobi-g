#creating dictionnary
daysinmonth ={
1:31,
2:28,
3:31,
4:30,
5:31,
6:30,
7:31,
8:31,
9:30,
10:31,
11:30,
12:31,}
#Input handling
month_entered=int(input("Enter the month number:"))
#check and output
if 1 <=month_entered<= 12:
    if month_entered == 2:
        is_leap = input("is it a leap year? (yes/no) ")
        if is_leap == "yes":
            days = 29
            print(f"valid month number and it has {days} days.")
        elif is_leap == "no":
            days = 28
            print(f"valid month number and it has {days} days.")
    else:
        print(f"valid month number and it has{daysinmonth[month_entered]}days.")
else:
    print("incorrect month number")
    