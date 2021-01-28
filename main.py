name = input("Enter your name : ")
age = int(input("Enter your age : "))
try:
    name = input("Enter your name : ")
    age = int(input("Enter your age : "))
except ValueError:
    name = "unknown"
    age = "unknown"
finally:
    print(f"Name : {name}\n"
          f"Age : {age}")

