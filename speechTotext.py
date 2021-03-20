
import speech_recognition as sr 



r = sr.Recognizer() 


mic_list = sr.Microphone.list_microphone_names()

##print(mic_list)


 
with sr.Microphone(device_index = 1, sample_rate = 48000, chunk_size = 1024) as source: 

	 
    r.adjust_for_ambient_noise(source) 
    print("Say Something")
	
    audio = r.listen(source) 
		
    try: 
        text = r.recognize_google(audio) 
        print ("you said: " + text)
    except:
        print("Something error ")
