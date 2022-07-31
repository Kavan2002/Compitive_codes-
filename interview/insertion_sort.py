def insertion_sort(a):

    for i in range(1,len(a)):
        min1 = a[i]
        # print("min : ",min1)
        j=i-1
        while j>=0 and min1 < a[j]:

            # print("i:",i,"j+1",a[j+1],",j:",a[j])
            a[j+1] = a[j]
            j=j-1


        a[j+1] = min1
        # print(a)
    print("insertion sort final : ",a)

if __name__ == "__main__":
    a=[12, 11, 13, 5, 6,18,2,8,1]
    insertion_sort(a)

