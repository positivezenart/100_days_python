#Write a program that switches the values stored in the variables a and b.
def switch_values(a,b):
     k=a
     a=b
     b=k
     print(f"value of a is {a}")
     print(f"value of b is {b}")
    
a= input("a:")
b=input("b:")

switch_values(a,b)

