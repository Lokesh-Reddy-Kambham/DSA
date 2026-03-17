#Approach 1
def reverseArray(arr):
    i ,j = 0 ,len(arr)-1
    while i<=j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr

#Approach 2
def reverseArray(arr):
    i , j = 0 , -1
    for k in range(len(arr)//2):
        arr[i] , arr[j] = arr[j] , arr[i]
        i += 1
        j -= 1
    return arr

b = [1,4,3,2]
print(reverseArray(b))