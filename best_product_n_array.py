def best_product_array_except_self(nums):
	print("test:", nums)
	n = len(nums)
	suffix = [1] * n
	prefix = [1] * n

	for i in range(1, n):
		prefix[i] = prefix[i-1] * nums[i-1]

	for i in range(n-2, -1, -1):
		print("sff", i)
		suffix[i] = suffix[i+1] * nums[i+1]

	print("prefix: ", prefix)
	print("suffix: ", suffix)
	output = [1] * n
	for i in range(n):
		output[i] = prefix[i] * suffix[i]
	return output

if __name__ == "__main__":
	result = best_product_array_except_self([1,2,3,4])
	print(result)