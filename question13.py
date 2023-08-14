from functools import reduce

class Number:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def get(self):
        return self.numbers
    
    def change_original_values(self,func:lambda x:x):
        new_numbers= list(map(func,self.numbers))
        return new_numbers
        
    def filter_values(self,filter_func:lambda x:x):
        filtered_numbers = list(filter(filter_func,self.numbers))
        return filtered_numbers

    def compound_the_numbers(self,reduce_func:lambda compound,d:compound + d):
        compounded_value = reduce(reduce_func,self.numbers)
        return compounded_value

    def sort(self):
        self.numbers.sort()
        return self.numbers


num = Number([2, 5, 1, 66, 22, 11, 10])
print("Numbers",num.get())
print("New Values : ",num.change_original_values(func=lambda x:x*2))
print("Filtered Values : ",num.filter_values(filter_func=lambda x:x%2==0))
print("Compounded Value : ",num.compound_the_numbers(lambda x,y:x+y))
print("Sorted List : ",num.sort())

