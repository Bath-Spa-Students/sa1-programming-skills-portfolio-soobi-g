# getting input
first_name = input("what's your first name? ")
second_name = input("what's your second name? ")

hometown = input("from where you are? ")

# validating age
age = input("how old are you? ")
while not age.isdigit():
    age = input("enter your number age: ")

#recording infos
info ={"name": first_name + " " + second_name,
       "age": age,
       "hometown": hometown}
#getting the result
print(f"Name: {info.get('name')} \nAge: {info.get('age')} \nHometown: {info.get('hometown')}")