def threecal(a,b,c):
    
    L = [a,b,c]
    
    ma = max(L)
    mi = min(L)
    su = sum((a,b,c))
    me = sum(L)/3
    
    return (ma, mi, su, me)

def absf(n):
    if n < 0:
        return n*(-1)
    else:
        return n

def circleArea(r):
    
    pi = 3.14    
    return pi*r**2

class Add:
    def add(self, n1, n2):
        return n1+n2
    
class Multiply:
    def multiply(self, n1, n2):
        return n1*n2
    
class Calculator(Add, Multiply):
    def sub(self, n1, n2):
        return n1 - n2

class Note:
    
    def __init__(self, contents=''):
        self.contents = contents
        
    def write_contents(self, contents):
        self.contents = contents
        
    def remove_contents(self):
        self.contents = ''
        
    def __str__(self):
        print('객체를 프린트할 때 실행되는 함수')
        return self.contents