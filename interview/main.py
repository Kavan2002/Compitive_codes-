from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from quick_sort import quickSort
from binary_search import search
arr=[11,88,66,77,44,33,22,55,99]
target = 99
res = search(arr,target)
print(target," position (starting with 0): ",res)
bubble_sort(arr)
insertion_sort(arr)
selection_sort(arr)
merge_sort(arr)
print("mergesort final : ",arr)
quickSort(arr,0,len(arr)-1)
print("quicksort final :",arr)