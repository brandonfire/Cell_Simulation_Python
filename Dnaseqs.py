class Dnaseq():
    Seq = ''
    Length = 0
    Rseq = ''
    BC = { 'A' : 0, 'T' :0, 'C':0 , 'G':0}
    GC = 0.00
    Rnaseq = ''

    def __init__ (self, newseq):
        self.Seq = newseq.upper()
        for x in self.Seq:
            
            if x != 'A' and x != 'T' and x != 'C' and x != 'G':
                print 'This is not a DNA sequence'
                return False
                break
    def Fulllen (self):
        self.Length = len(self.Seq)
        print "The DNA full length is " + str(self.Length)
        return self.Length
    def Revcom(self):
        
        for x in self.Seq:
            if x == 'A':
                self.Rseq += 'T'
            elif x == 'T':
                self.Rseq += 'A'
            elif x == 'C':
                self.Rseq += 'G'
            else:
                self.Rseq += 'C'
            
        print "The reverse complement sequence is"
        print self.Rseq
        return self.Rseq
    def basecom(self):
        self.BC['A'] = self.Seq.count('A')
        self.BC['T'] = self.Seq.count('T')
        self.BC['C'] = self.Seq.count('C')
        self.BC['G'] = self.Seq.count('G')
        print "The base composition:"
        print self.BC
        return self.BC
    def gccontent(self):
        self.GC = (self.BC['G'] + self.BC['C'])*1.0/self.Length
        print "The CG conten is  " + str(self.GC * 100) + '%'
        return self.GC
    def findseq(self,seqwant):
        n = 0
 
        while n < len(self.Seq):
            n = self.Seq.find(seqwant,n)
            if n == -1:
                print " Finding process over!"
                break
            print "There is " + seqwant + " at position " + str(n)
            n += 1
    def translate(self):
        self.Rnaseq = self.Seq.replace( 'T', 'U')
        print "Rna sequence is " + str(self.Rnaseq)
        return self.Rnaseq

        

        
                
    
