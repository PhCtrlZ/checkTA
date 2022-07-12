import speech_recognition
import pyttsx3
#xử lí dữ liệu đầu vào
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain=""
#nhập từ mà bạn muốn kiểm tra
check=input("nhập vào từ mà bạn muốn kiểm tra(viết thường hết nhé):")
#xử lí đầu ra và cho kết quả 
while True:
	with speech_recognition.Microphone() as mic:
		 print("Trợ lí ảo : i'm listening")
		 audio = robot_ear.record(mic,duration=6)
	print("Trợ lí ảo :...")
	try:
	     you = robot_ear.recognize_google(audio)
	except:
		 you =""
	print("You:" + you)
	if you=="":
		print("Tôi ko thể nghe thấy bạn vui lòng thử lại")
	if check==you:
		print("bạn đã nói đúng từ :"+check)
	if check!=you:
		print("bạn nói sai rồi hãy thử lại sau nhé")
	elif "bye" in you:
		robot_brain="Goodbye and see you again"
		print("Trợ lí ảo :"+robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	print("Trợ lí ảo:"+robot_brain)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()
