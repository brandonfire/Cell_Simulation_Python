class biostat():
    import math
    ave1 = 0
    ave2 = 0
    Ssubpsquar = 0
    T = 0
    #Need to assign a start number for adding i together
    def total(self,l):
        x=0.0
        for i in l:
            x+=i
        return x
    def sqtotal(self,l):
        x=0.0
        for i in l:
            x+=pow(i,2)
        return x
    def ave(self,l):
        x=0.0
        for i in l:
            x += i
        return x/len(l)
    # To use ave I need to add self.
    
    def __init__(self,a,b):
        self.ave1=self.ave(a)
        self.ave2=self.ave(b)
        ta=self.total(a)
        tb=self.total(b)
        sta=self.sqtotal(a)
        stb=self.sqtotal(b)
        self.Ssubpsquar=(sta-pow(ta,2)/len(a)+stb-pow(tb,2)/len(b))/(len(a)+len(b)-2)
    #make sure use float and use self.math
        self.T = (self.ave1-self.ave2)/self.math.sqrt(self.Ssubpsquar*(1.0/len(a)+1.0/len(b)))
        print "T eqals",self.T
