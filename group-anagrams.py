def group_anagrams(strs):
    print("test strs: ", strs)
    memory = {}
    for i in strs:
        split_sort = "".join(sorted(i))
        if split_sort in memory:
            memory[split_sort].append(i)
        else:
            memory[split_sort] = [i]
    return memory.values()

if __name__ == "__main__":
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(result)