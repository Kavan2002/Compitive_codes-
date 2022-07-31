from insertion_sort import insertion_sort
from selection_sort import selection_sort
def bubble_sort(a):

    for i in range(0,len(a)):

        for j in range(0,len(a)-i-1):

            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]

    print("bubble_sort final : ",a)

if __name__ == "__main__":
    a=[7,9,5,6,3,2,1,7,5,1]
    bubble_sort(a)
    insertion_sort(a)
    selection_sort(a)
