def interpolation(arr,c1,lo,hi):
    while(lo < hi):
        b=hi-lo
        b1=arr[hi]-arr[lo]
        if (b1!=0):
            b=int(b/b1)
        else:
            b=0
        b1=b*(c1-arr[lo])
        pos=lo+b1
        if(arr[pos]==c1):
            return pos
        if(arr[pos]>c1):
            hi=pos-1
        else:
            lo=pos+1
    return -1        
def low(arr,c1,lo,hi):
    a=True
    while(a):
        pos=interpolation(arr,c1,lo,hi)
        c1=c1-1
        print c1
        if(pos!=-1):
            a=False
        if(c1==0):
            a=False
            pos=-1
    if(pos!= -1):
        print c1
        num1=arr[pos]
        num2=m-num1
        pos2=interpolation(arr,num2,pos+1,hi)
        if(pos2==-1):
            low(arr,c1,lo,hi)
        else:
            if(arr[pos]>arr[pos2]):
                print "%r %r" %(pos2+1,pos1+1)
            else:
                print "%r %r" %(pos+1,pos2+1)
    else:
        print "end"
    
    
m =input()
n =input()
arr=[]
while (len(arr)< n):
    arr.append(input())
arr.sort()
print arr
lo=0
hi=n-1
c1=int(m/2)
low(arr,c1,lo,hi)

    


