programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
                          "Function": "A piece of code that you can easily call over and over again."}

empty_dictionary ={}
programming_dictionary["name"]= "My name is mj"

print(programming_dictionary)

for i in programming_dictionary:
    print(programming_dictionary[i])

programming_dictionary = empty_dictionary
print(programming_dictionary)