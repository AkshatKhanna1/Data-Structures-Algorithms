def mooreVoting(arr):
    value=arr[0]
    count=1
    n=len(arr)
    for i in arr[1:]:
        if i==value:
            count+=1
        else:
            if count==1:
                value=i
            else:
                count+=1
    itr=0
    for i in arr:
        if i==value:
            itr+=1
            
    if itr>n//2:
        return value
    return -1
