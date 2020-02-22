def Quick(theSeq):
    last=len(theSeq)-1
    first=1
    pivot=0
    while(first<=last):
        while(first<last and theSeq[pivot]>theSeq[first]):
            first=first+1

        while(first<=last and theSeq[pivot]<=theSeq[last]):
            last=last-1
        
        if(first<=last and theSeq[first]>theSeq[last]):
            theSeq[first] , theSeq[last] = theSeq[last],theSeq[first]
    theSeq[pivot],theSeq[last]=theSeq[last],theSeq[pivot]
    return(theSeq)

seq=[10,23,51,18,4,31,5,13]
print(Quick(seq))        


        





    
