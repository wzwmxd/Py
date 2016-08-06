"""
number=range(10)
size=len(number)
evens=[]
i=0
while i<size:
    if i%2==0:
        evens.append(i)
    i+=1
print(evens)

print([i for i in range(10) if i%2==0])

seq=["one","two","three"]
for i,element in enumerate(seq):
    seq[i]='%d: %s'%(i,seq[i])
print(seq)

class MyIterator(object):
    def __init__(self,step):
        self.step=step
    def next(self):
        if self.step==0:
            raise  StopIteration
        self.step-=1
        return self.step
    def __iter__(self):
        return self
for el in MyIterator(4):
    print(el)
    """


def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


fib = fibonacci()
for i in range(100):
    print(fib.next())
    print("\n")
