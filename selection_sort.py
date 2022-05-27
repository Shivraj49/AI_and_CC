
def sel_sort(arr):
    length = len(arr)
    for i in range (length-1):
        for j in range (i+1,length):
            if arr[j] < arr[i]:
                arr[i],arr[j]=arr[j],arr[i]

    return arr

#Main Function
arr=[10,2,45,67,23,6]
sel_sort(arr)
print(arr)
