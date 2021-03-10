class Squares:
    def __init__(self,number):
        self.number=number
    def __iter__(self):
        self.count=0
        return self
    def __next__(self):
        if self.count <self.number:
            output= self.count**2
            self.count+=1
            return output
        else:
            raise StopIteration
for square in Squares(21):
    print(square)
import sys
print(sys.getsizeof(Squares(5)))
print(sys.getsizeof(Squares(5000000)))