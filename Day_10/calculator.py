from art import *
print(logo)


def calcualtor(f_number, operator, n_number):
    if operator == '+':
        add_operator = f_number + n_number
        return add_operator,f_number,n_number,operator
    elif operator == '-':
        sub_operator = f_number - n_number
        return sub_operator,f_number,n_number,operator
    elif operator == '*':
         mul_operator = f_number * n_number
         return mul_operator,f_number,n_number,operator
    elif operator == '/':
        div_operator = f_number / n_number
        return div_operator,f_number,n_number,operator

def input_values():        
    print("welcome to the calculator")        
    f_number = float(input("whats the first number? \n"))
    print(" + \n - \n * \n /")
    should_continue = True
     
    while should_continue:
        print(" + \n - \n * \n /")
        operator = input("Please,Pick an operator from line above? \n")
        n_number = float(input("Whats the next number? \n"))
        output = calcualtor(f_number, operator, n_number)
        print(f"{output[1]} {output[3]} {output[2]} = {output[0]}") 
        wanna_continue = input(" Do you want to continue the same calculation with returned output, press yes, if you want fresh calulcation , type no \n")
        if wanna_continue == 'yes':
           f_number = output[0]
        else: 
            should_continue = False
            input_values()
        
input_values()
        
    