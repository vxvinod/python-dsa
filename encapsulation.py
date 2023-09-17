class AudioCall:
	
	# Initialize method, this is triggered when class is initialized/
	def __init__(self):
		print("Audio call init called")

	# Public method.
	def call(self):
		print("Call method")
		self.__audio_call_history()
	
	# Private method
	def __audio_call_history(self):
		print("Audio call history")
	
	# Protected method
	def _audio_call_functionality(self):
		print("Audio call functionality called")

class VideoCall(AudioCall):   # Pass the parent class argument to child class for inheriting the parent class.
	def __init__(self):
		print("Video call init called")
		super().__init__()

	def call(self):
		print("Video Call method")
		super()._audio_call_functionality()  # calling protected method.
		super().call() # calling public method
you = AudioCall()
you.call()
you._audio_call_functionality()
#you.__audio_call_history() # This will throw error since private method cannot be accessed outside.

video_you = VideoCall()
video_you.call()
