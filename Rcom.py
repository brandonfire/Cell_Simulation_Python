
    Rcom = ""
    
    for x in seq[::-1]:
            if x == 'A':
                Rcom += 'T'
            elif x == 'T':
                Rcom += 'A'
            elif x == 'C':
                Rcom += 'G'
            else:
                Rcom += 'C'
    start = []
    while True:
        z = Rcom.find("ATG")
        if z == -1:
            break
        start.append(z)
    
    stop = 0
    for s in start:
        
        for i in range(s,n,3):
            if i+3 > n:
                break
            if Rcom[i:i+3] == "TAA" or Rcom[i:i+3] == "TAG" or Rcom[i:i+3] == "TGA":
                stop = i+3
                break
        if stop != 0:
            startend.append([-s,-stop])
    return startend
    
