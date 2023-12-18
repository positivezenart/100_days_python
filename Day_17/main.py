class UserInterface: #creating a class, use passcall case
     def __init__(self,user_id,user_name): # constructing a constructor
         self.user_id = user_id          #creating a variable or attributes
         self.user_name = user_name
         self.followers =0 
         self.following = 0#intializing a variable
    
     def follow(self,user):
         user.followers +=1
         self.following  += 1
        
 
user_1 = UserInterface(4,"mahesh") #building an object
user_2 = UserInterface(6,"ramu")

print(user_1.user_id) #

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
