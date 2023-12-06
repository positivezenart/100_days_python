from art import *
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(text,shift,direction):
        value = ""
        if direction == 'decode':
            shift *= -1
        for letter in text:
            if letter in alphabet:
               position = alphabet.index(letter)
               new_position = position + shift
               value += alphabet[new_position %26]
            else:
                value += letter
    
        print(f"The {direction} value is {value}") 

while True:
    reply = input("Do you want to continue yes or no? \n").lower()
    if reply =='yes':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if shift > 26:
           shift = shift % 26
           print(shift)
        ceaser(text,shift,direction)
    elif reply =='no':
        print("Good Bye!")
        break
    else:
        print("please select yes or no only")
        continue
       
        
