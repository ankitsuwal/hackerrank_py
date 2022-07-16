class One():
    def __init__(self, v1, v2) -> None:
        self.v1 = v1
        self.v2 = v2
        
    def func1(self):
        return self.v1 + self.v2
    
    def func2(self):
        return self.v1 * self.v2
    
class Two(One):
    def __init__(self, v1, v2) -> None:
        super().__init__(v1, v2)
    
    def func1(self):
        return self.v2 - self.v1
    
    def func3(self):
        return self.v2 // self.v1
    

two_obj = Two(10, 2)
print(two_obj.super.func1())