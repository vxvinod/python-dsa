def top_k_elements(nums, k):
    print("test nums: ", nums)
    print("test k: ", k)
    memory = {}
    output = []
    for i in nums:
        memory[i] = memory.get(i, 0) + 1
        if memory[i] >= k:
            if i not in output:
                output.append(i)
    return output[:k]


if __name__ == "__main__":
    result = top_k_elements([3,3,3,3,3,2,2,2,2,2,1,1,1,1,1], 2)
    print(result)