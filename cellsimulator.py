

import random

# Gene class (MT and KGS)

class Gene():
    name = ''
    chrom = ''
    start = 0
    end = 0
    strand = '+' 
    aaseq = '' # Translation is stored, since it is computationally expensive

    # method to retrieve the gene given its name
    def describe(self):
	print "Name: ", self.name
        print "Position: ", self.chrom, ':', self.start, '-', self.end
	print "Strand: ", self.strand
        print "protein length:", len(self.aaseq)

# Chromosome class 

class Chrom():
    seq = ""
    length = 0
    cell = False

    # Start and stop signals on forward and reverse strand
    start = ["ATG"]
    stop = ["TAA", "TAG", "TGA"]              
    rstart = ["TTA", "CTA", "TCA"]
    rstop = ["CAT"]

    def __init__(self, cell, n):
        self.randseq(n)         # Initialize chromosome to random sequence
        self.cell = cell        # Backpointer to cell

    def randseq(self, n):
        self.seq = ""
        for x in range(n):
            self.seq = self.seq + random.choice("ACGT")
        self.length = n

    def findstartplus(self, s):
        return self.seq.find(self.start[0], s)

    def findendplus(self, s):
        while True:
            t = self.seq[s:s+3]
            if t in self.stop:
                return s
            s = s + 3
            if s > self.length:
                return -1
    
    def findstartminus(self, s):
        return self.seq.find(self.rstop[0], s)

    def findendminus (self, s):
        while True:
            t = self.seq[s:s+3]
            if t in self.rstart:
                return s
            s = s - 3
            if s < 0:
                return -1
    
    def findgenes(self):
        s = -1
        while True:
            s = self.findstartplus(s+1)
            if s == -1:
                break
            e = self.findendplus(s+3)
            if e > 0:
                print "orf found at ", s, e
                print self.seq[s:e+3]

    def findrgenes(self):
        s = -1
        while True:
            s = self.findstartminus(s+1)
            if s == -1:
                break
            e = self.findendminus(s-3)
            if e > 0:
                print "orf found at ", s, e
                print self.seq[e:s+3]
        
# Main cell class 

class Cell():
    chrom = False    # Chromosome object
    genecounter = 0  # Number of known genes
    genes = dict()   # Dictionary to store the genes we find in the sequence

    def __init__(self, chromlength):
        self.chrom = Chrom(self, chromlength) # Create chromosome object and store it

    def describe(self):
	print 'Chromosome length:', len(self.chrom.seq)
        print 'Number of genes:', len(self.genes)     

    # Method to add a gene to the set of genes in this cell
    def newgene(self, chrom, start, end, strand):
        g = Gene()
        g.chrom = chrom
        g.start = start
        g.end = end
        g.strand= strand
        self.genecounter += 1
        g.name = 'gene'+str(self.genecounter)
        self.genes[g.name]=g 
        return g

    # Method to return a gene given its name
    def findGene(self, genename):
        if genename in self.genes:
            return self.genes[genename]
        else:
            print 'gene not found'
            return False

	

# Standalone function to translate
# DNA into amino acid sequence 

gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W'}

def translate(dna):
    n = len(dna)
    aa = ''
    for i in range(0,n,3):
        aa += gencode[dna[i:i+3]]
    return aa
    
# Testing function

def test():
    c = Cell(999)
    return c

