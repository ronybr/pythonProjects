import speech_recognition as sr
import pyttsx3


#Initialize the recognizer
recognizer = sr.Recognizer()

#Function to convert text to speech
def speak_text(command):
    #Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

#Loop infinitely for user to speak
while(1):
    #Exception handling to handle exceptions at the runtime
    try:
        #Use the microphone as source for input
        with sr.Microphone() as source2:

            """
            Wait for a second to let the recognizer adjust the
            energy threshold based on the surronding noise level
            """
            recognizer.adjust_for_ambient_noise(source2, duration=0.2)

            #Listen for the user's input
            audio2 = recognizer.listen(source2)

            #Using google to recognize audio
            my_text = recognizer.recognize_google(audio2)
            my_text = my_text.lower()

            print("Did you say: " + my_text)
            speak_text(my_text)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown error occured")