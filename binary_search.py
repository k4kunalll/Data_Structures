def bb(arry,n):

    l = 0
    r = len(arry)-1

    while r >= l:
        mid = (l+r)//2

        if a[mid] == n:
            return(mid)

        elif a[mid] > n:
            r = mid-1
            
        elif a[mid] < n: 
            l = mid+1
        
    else:
        return(-1)
        



a = [1,2,3,4,5]
n = 22
print(bb(a,n))