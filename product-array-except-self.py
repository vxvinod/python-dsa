import math
def product_array_except_self(nums):
	print("test nums: ", nums)
	output = []
	for i in nums:
		left_mult = nums[i:]
		right_mult = nums[:i-1]
		print("$$$$$$$$$$$")
		print(left_mult)
		print(right_mult)
		output.append(math.prod(left_mult)*math.prod(right_mult))
	return output

if __name__ == "__main__":
	result = product_array_except_self([1,2,3,4])
	print(result)