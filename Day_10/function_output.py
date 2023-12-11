def format_name(first_name,last_name):
    f_name = first_name.title()
    l_name = last_name.title()
    Final_name = f_name + " " + l_name
    return Final_name,l_name,f_name


first_name = input("Enter your first name? \n" ).lower()
last_name = input("Enter your last name? \n").lower()

name = format_name(first_name,last_name)

print(f"Titalized name is : {name[0]}")