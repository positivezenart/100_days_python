def prime_checker(number):
    is_prime = True
    if number == 1 or number ==0:
       print("its Not a prime number")
    elif number > 1:
      for i in range(2,number):
         if (number % i) == 0:
            is_prime = False
            break
      if is_prime:
        print("Its a prime number.")
      else:
        print("Its not a prime number")


n = int(input("Enter the prime number?")) # Check this number
prime_checker(number=n)