def search(nums, target) :

    left,right=0,len(nums)-1

    while left <=right:

        mid_term = left+(right-left)//2
        # print(nums[mid_term])
        if nums[mid_term] == target:
            return mid_term

        elif nums[mid_term] > target:
            right = mid_term -1
        else:
            left = mid_term+1
    return -1

if __name__ == "__main__":
    arr=[2,5,6,1,8,34,7,22,9]
    arr.sort()
    target = 1

    res = search(arr,target)
    # if res ==-1:
    #     print("not found")
    # else:
    print("position :",res)