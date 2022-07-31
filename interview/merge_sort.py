

def merge_sort(arr):

    if len(arr)>1:

        mid = len(arr)//2

        left_arr = arr[:mid]
        right_arr = arr[mid:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i=j=k=0

        while i<len(left_arr) and j<len(right_arr):

            if left_arr[i] > right_arr[j]:

                arr[k] = right_arr[j]
                j=j+1
            else:
                arr[k] = left_arr[i]
                i=i+1

            k=k+1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            k=k+1
            i=i+1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            k = k + 1
            j = j + 1


        # print("merge sort : ",arr)


if __name__ =="__main__":
    arr=[11,88,66,77,44,33,22,55,99]
    merge_sort(arr)
    print("final merge sort : ",arr)