

# best case : n*logn
# worst case : n*2

# first we need an proper place for pivot element :
# we chose mainly middle , first or last element as pivot
# then iterate loop from both starting(i) and ending(j) index for
# i is searching for element which is greater than pivot
#  j is searching for element which is smaller than pivot
# increment i untill you find element greater than pivot
# decrememt j unitill you find element smaller than or equal to pivot
# exchange both

def partition(arr,left,right):
    pivot = arr[right]
    i=left
    j=right-1

    # Traverse through all elements
    # compare each element with pivot
    while i<j:

        # i looks for bigger element than pivot
        while i<right and arr[i] <pivot :
            i=i+1

        # j look for smaller elements than pivot
        while j > left and arr[j]>=pivot :
            j=j-1

        # if i and j didn't cross each other than swap both ith and jth element
        if i <j :
            arr[i],arr[j] = arr[j],arr[i]

    if arr[i] > pivot :
        arr[i],arr[right] = arr[right],arr[i]  #swap pivot & i


    return i
def quickSort(arr,left,right):
    if left < right :
        partition_pos = partition(arr,left,right)
        quickSort(arr,left,partition_pos-1) #left side of pivot
        quickSort(arr,partition_pos +1,right) #right side of pivot


if __name__=="__main__":
    arr=[22,11,77,66,33,55,44,99,88]
    quickSort(arr,0,len(arr)-1)
    print("quick sort final : ",arr)
