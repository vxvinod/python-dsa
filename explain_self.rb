class ExplainSelf:

	def __init__(self, name):
		self.contact_name = name
		print("self id is=====", id(self))
	def message(self, message):
		self.message = message 
		print("sent message:", self.message, "to ", self.contact_name)

	def send_photo(self, photo, message):
		self.photo = photo
		self.message = message
		print("sent photo with message:", self.message, "photo:", self.photo, "to ", self.contact_name)

	def last_sent_message(self):
		print("Last sent message is:",self.message)


its_me = ExplainSelf("Elon Musk")
print("its_me object id", id(its_me))
its_me.message("Hello man!!!")
its_me.send_photo("Twitter photo", "Why did you changed the name to X")
its_me.last_sent_message()