#this is a word count function
def wordcount(filename):
#open filename file first
    f = open(filename)
    l=0
    n=0
#make a loop to count lines and word counts
    for line in f:
        l = l + 1
        n = n + len(line)
#close file and return lines and word counts as a list
    f.close()
    print "File " + filename + ' contains ' + str(l) + ' lines and ' +str(n) + " words."

    return [ l , n]


def randseq(filename, name, n):
    import random
    with open(filename, 'w') as f:
        f.write('>' + name)
        
    
        
        for x in range(n):
            f.write(random.choice('ATCG'))
            if x%60 == 0:
                f.write('\n')
                
        f.write('\n')


        
            
        
