def selection_sort(a):

    for i in range(len(a)):

        min_index = i
        for j in range(i+1,len(a)):

            if a[min_index] > a[j]:
                min_index=j

        a[min_index],a[i] = a[i],a[min_index]

    print("selection sort : ",a)

if __name__ == "__main__":
    arr=[1,8,2,9,6,4,3,18,0]
    selection_sort(arr)