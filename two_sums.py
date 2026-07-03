def two_sums(nums, target):
    print("test nums: ", nums)
    print("test target: ", target)
    output = []
    for i in range(len(nums)-1):
        print(i)
        for j in range(i+1, len(nums)):    
            if ((nums[i] + nums[j] == target)):
                output.append([i, j])
    print(output)
    return output
#two_sums([2, 7, 11, 15], 9)


def two_sumss(nums, target):
    output = []
    is_found = {}
    for i in (range(len(nums)-1)):
        is_found[nums[i]] = i
        print(is_found)
        if(target > nums[i]):
            check_val = target - nums[i]
            print("checkval", check_val)
            if check_val in is_found:
                output.append([i, is_found[check_val]])

    print(output)
    return output

two_sumss([2, 7, 11, 15], 9)