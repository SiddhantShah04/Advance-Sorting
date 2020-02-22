def quickSort(theSeq):
    n = len(theSeq)
    reQuickSort(theSeq,0,n-1)

def reQuickSort(theSeq,first,last):
    pivot =theSeq[first]
    pos=partitionSeq(theSeq,first,last)
    recQuickSort(theSeq,first,last,pos-1)
    reQuickSort(theSeq,pos+1,last)

def partitionSeq(theSeq,first,last):
    pivot=theSeq[first]
    left=first+1
    right=last
    while(left<=right):
        while(left<right and theSeq[left]<pivot):
            left=left+1
        while(right >=left and theSeq[right]>=pivot):
            right=right-1

        if(left<right):
            tmp=theSeq[right]
            theSeq[left]=theSeq[right]
            theSeq[right]=tmp

    return(right)  
seq = [10,23,51,18,4,31,5,13]
quickSort(seq)
