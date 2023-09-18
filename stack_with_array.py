class Stack:
	
	def __init__(self, list):
		self.list = list  # Define the instance variable, which can be accessed across the class.

	def push(self, value):
		self.list.append(value)  # push value to the array.
		print(value, "pushed successfully to stack")

	def pop(self):
		last_val = self.list.pop() # remove the last element of the array
		print(last_val, "is removed successfully")
	
	def top(self):
		x = len(self.list)   #Find the length of the array.
		return self.list[x-1]  # this is how value is returnd from method call.


st = Stack([1,2,3,4])
st.push(5)
st.push(6)
st.pop()
print(st.top(), "is the top of the stack")