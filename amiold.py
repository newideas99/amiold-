name = input("what is your name?")
age = input("what is your age?")

print(f"My name is {name} i am {age} years old")

age = int(age)

amiold = input ("Do you want to know if you're old?")

if amiold == "yes":
    if age < 70:
        print("you are young")
    else: 
        print("your are old")
else:
    print(f"Okay sorry for asking {name}")