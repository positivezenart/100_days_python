for i in range(1,100+1):
    if i % 5 == 0 and i % 3 == 0:
        i = 'fizzbuzz'
        print(i)
    elif i % 3 == 0:
       i = 'fizz'
       print(i)
    elif i % 5 == 0:
        i = 'buzz'
        print(i)
    else:   
        print(i)