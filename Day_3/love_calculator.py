from collections import Counter
name = input("enter your name \n").lower()
lover_name = input("enter your crush name \n").lower()

counter_you = Counter(name + lover_name)
true = str(counter_you['t'] + counter_you['r'] +counter_you['u'] + counter_you['e'])
love =str(counter_you['l'] + counter_you['o'] +counter_you['v'] + counter_you['e'])
print(true + love)