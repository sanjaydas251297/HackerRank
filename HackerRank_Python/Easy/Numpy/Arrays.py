import numpy

def arrays(arr):
    b=numpy.array(arr,float)
    new_lst = b[::-1] 
    return(new_lst) 

#or b=numpy.array(arr[::-1],float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)