import speech_recognition as sr
from dynamic_chatbot import dynamic_chatbot


r = sr.Recognizer()
m = sr.Microphone()

def sound_input():
    done = False
    try:
        print("A moment of silence, please...")
        with m as source: r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        while not done:
            print("Say something!")
            with m as source: audio = r.listen(source)
            #print("Got it! Now to recognize it...")
            try:
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio)

                # we need some special handling here to correctly print unicode characters to standard output
                if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                    text=  ((value).encode("utf-8"))
                else:  
                    text = (value)
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
            if text == "stop":
                done = True
            else:
                print(text)
                dynamic_chatbot(text)
                input("")
    except KeyboardInterrupt:
        pass
    

        