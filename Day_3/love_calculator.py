from collections import Counter
print("welcome to the love calculator")
name = input("enter your name \n").lower()
lover_name = input("enter your crush name \n").lower()

counter_you = Counter(name + lover_name)
true = str(counter_you['t'] + counter_you['r'] +counter_you['u'] + counter_you['e'])
love =str(counter_you['l'] + counter_you['o'] +counter_you['v'] + counter_you['e'])
final_score = true + love

if final_score <10 or final_score > 90:
    print(f"Your score is {final_score} ,you go together like coke and mentos.")
elif final_score > 40 and final_score < 50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}")