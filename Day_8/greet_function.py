name = input("enter the name?\n")
location =input("Where he must be from?\n")
#NAME IS THE PARAMETER, VALUE WE PASS IS THE ARGUMENT
def greet(name,location):
    print(f"Hello {name}!")
    print("Good Morning!")
    print(f"are you from {location} ?")

 #keyword arguments can overcome positional arguments issue   
greet(location = location,name =name)
