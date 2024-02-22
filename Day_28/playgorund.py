#unlimited positional arguments 
def add(*args):
    sum=0
    for i in args:
        sum =sum +i
    return sum

print(add(1,2,3,4))

#unlimited keyword arguments
def calculate(n,**kwargs):
     n += kwargs.get("add")
     return n

print(calculate(1,add=3,multiply=4))