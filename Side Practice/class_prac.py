class MyTuple:
    def __init__(self, first_value, second_value):
        self.first_value = first_value
        self.second_value = second_value
        
    def __str__(self):
        return f"({self.first_value}, {self.second_value})"
    
    def get_first(self):
        return self.first_value
    
    def get_second(self):
        return self.second_value
    
    def set_first(self, value):
        self.first_value = value
        
    def set_second(self, value):
        self.second_value = value
        
        
def main():
    
    t1 = MyTuple(1,2)
    t2 = MyTuple(1,3)
    t3 = MyTuple(1,4)
    t4 = MyTuple(1,5)
    t5 = MyTuple(1,6)
    
    tuple_list = [t1, t2, t3, t4, t5]
    
    for tup in tuple_list:
        print(tup)
        
        
main()
    
    
            