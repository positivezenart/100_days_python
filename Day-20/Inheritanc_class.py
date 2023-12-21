class ANIMAL:
    def __init__(self):
       self.num_of_eyes = 2
       
    def breathe(self):
        print("Inhale,Exhale")

class FISH(ANIMAL):
    def __init__(self):
        super().__init__()
    
    def breathe(self):
        super().breathe()
        print("underwater")
        
    def swim(self):
        print("move like a water")
        
nemo = FISH()
nemo.swim()
nemo.breathe()

#this is called as inheritance, inherting from main class
