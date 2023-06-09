#1
lst=[1,2,3,4,5,6,7,8,9,10]
print(iter(lst))
class OddIterator():
    def __init__(self, data):
        self.data=data
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index>=len(self.data):
            raise StopIteration
        value=self.data[self.index]
        self.index+=2
        return value
for num in OddIterator(lst):
    print(num)




#2
class SquareGenerator():
    def __init__(self, n):
        if not isinstance(n, (int, float)):
            raise TypeError(":(")
        self.n=n
    def gen(self):
        for i in range(1, int(self.n)+1):
            yield i**2
try:
    for num in SquareGenerator(20).gen():
        print(num)
except TypeError as e:
    print(e)




#3
class ListIterator():
    def __init__(self, lst):
        self.lst=lst
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index>=len(self.lst):
            raise StopIteration
        value=self.lst[self.index]
        self.index+=1
        return value
for num in ListIterator(lst):
    print(num)



#4
def multiply_by():
    def zamk(n):
        n=n*n
        return n
    return zamk
zamk=multiply_by()
print(zamk(2))
print(zamk(5))