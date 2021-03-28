class penjumlahan():
    def __init__ (self,a,b):
        self.a=a
        self.b=b
    def plus1(self):
        x=self.a
        while x<=self.b:
            print(x)
            x+=1

    def fibonaci(self):
        def F():
            a,b = 0,1
            while True:
                yield a
                a, b = b, a + b
        def SubFib(startNumber, endNumber):
            for cur in F():
                if cur > endNumber: return
                if cur >= startNumber:
                    yield cur
        for i in SubFib(self.a, self.b):
            print (i)
    
    def kuadrat(self):
        x=self.a
        n=2
        while x<=self.b:
            print (x)
            x = self.a**n
            n+=1