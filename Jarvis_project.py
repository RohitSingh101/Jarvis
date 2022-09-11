from http import server
import pyttsx3 #pyttsx3 is a text-to-speech conversion library in Python.

#Speech Recognition allows computers to understand human language.
#You can then use speech recognition in Python to convert the spoken words into text, make a query or give a reply.
import speech_recognition as sr 
import datetime  #Datetime module supplies classes to work with date and time.
import wikipedia #It helps in executing commands related wikipedia.
import webbrowser #It helps in opening various websites on the browser
import os #Music player,getting date and time from the assistant is the working of os module.
import smtplib #Helps in sending Emails


#SAPI5 is the technology for voice recognition and synthesis provided by Microsoft. we can use windows inbuilt voice through Sepi5. 
engine=pyttsx3.init('sapi5') 
voices=engine.getProperty('voices') #It means we will get input in the form of voices.
'''through this getProperty('voices') we can choose that the voice we want will be of male or female, what will be the speed of voice we can 
set this manually with the help of getProperty()'''

print(voices[1].id) #There are two voices in windows which are inbuilt one is male and other is female.ID of male voices[0] and female is[1]
engine.setProperty('voice',voices[1].id) #Here we are defining that we will use female voice with the function 'setProperty()'


#Speak function is simply helping the system to repeat the text written in command in a voice.
def speak(audio):
    engine.say(audio) #This means we are giving command to out engine to speak 
    engine.runAndWait() #This function will make the speech audible in the system
    
#This function is simply wishing us on the basis of conditions we have given to it and with a default message.
def wishme():
      hour=int(datetime.datetime.now().hour)
      if hour>=0 and hour<12:
          speak('Good Morning')
      elif hour>=12 and hour<18:
          speak('Good Afternoon')
      else:
          speak('Good Evening')
      speak('I am caroline. Please tell me how may I help you sir')
    

#It takes microphone input from the user and returns string output
def takeCommand():
    
    r = sr.Recognizer() #We are initializing speech recognizer module here to recognize human voice.
    with sr.Microphone() as source: #We are assigning microphone as input device
        print("Listening...") 
        r.pause_threshold = 1  #Seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source) #Listen function helps in decoding the voice it received through microphone.


    '''We are writing the exception code because sometimes input voice is not clear or we re not connected to the internet or any other reason
       so the user will not suffer if code will have an exception handling part in itself  '''
    try:
        print("recognizing....") 

        # We have created an instance of recognizer class to use "Google Web Speech Api" and turn spoken language into text.
        query=r.recognize_google(audio, language='en-in') 
        print(f"user said: {query}\n") #Here we are printing that human voice query into text
        
    except Exception as e: #Identifying any kind of exception if occurs.
        print("Say that again please....")
        return "None"
    return query


#It sends email to a particular user.
'''REMINDER!! --> update this function by taking a dictionary and store Names as key and Email ID as attributes so that this function can send
Emails to anyone listed in that dictionary currently this is sending email to only a particular person'''
#THIS FUNCTION WILL NOT WORK CURRENTLY BECAUSE 'LESS SECURE APPS' SETTING IS NOT ENABLED IN THE EMAIL INSERTED IN IT.
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587) #Host name and Port name to access
    '''Extended HELO (EHLO) is an Extended Simple Mail Transfer Protocol (ESMTP)
     command sent by an email server to identify itself when connecting to another email server to start the process of sending an email.'''
    server.ehlo()
    server.starttls() #Puts the server into Tls(transfer layer security mode)
    server.login('rohitsingh38347@gmail.com','your-password')
    server.sendemail('rohtisingh38347@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishme()
    if 1:
        query=takeCommand().lower() #we are assigning takeCommand function to query.

        #Logic for executing tasks on query.

    #THIS IS THE WORKING OF WIKIPEDIA MODULE.
        if 'wikipedia' in query: #If the word wikipedia is included in query this If statement will take us to wikipedia.
            speak('Searching Wikipedia...') 
            query=query.replace('wikipedia',"") #this will replace the word wikipedia with blank space in the output.otherwise it will always take word 'wikipedia' as query
            results=wikipedia.summary(query, sentences=2) #This means that the result or summary will be same the response of query and it will be of 2sentences maximum.
            speak('According to Wikipedia')
            print(results) 
            speak(results) #assistant will speak the results


    #THIS IS THE WORKING OF WEBBROWSER MODULE.
        #Assistant will open this website.
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        #Assistant will open this website.
        elif 'open google' in query:
            webbrowser.open('google.com')

        #Assistant will open this website.
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        #Assistant will open this website.
        elif 'open hackerrank' in query:
            webbrowser.open('hackerrank.com')

        #Assistant will open this website.
        elif 'open gmail' in query:
            webbrowser.open('gmail.com')


    #THIS IS THE WORKING OF OS(OPERATING SYSTEM) MODULE.
        #REMINDER!! --> customize ths module with a piece of code in which a random number gets generated and a random song gets played 
        elif 'play music' in query:
            music_dir = 'd:\\jarvis songs'
            songs=os.listdir(music_dir) #Listdir func. give us the whole list of songs in this particular directory
            print(songs) #it will print the list of songs.
            os.startfile(os.path.join(music_dir,songs[0])) #os.startfile will open that music file,here we joined music_dir to song[0] then always the first song will play

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S") #"strf=string format" "now()=current date,time"
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query: #Opening VS code through jarvis 
            # REMINDER!!! --> WE CAN OPEN ANY APP OF DEKSTOP THROUGH JARVIS 
            codePath="C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\Code.exe" #Target location of VS code to get opened.
            os.startfile(codePath) #os.startfile will open VS code



    #THIS IS THE WORKING OF 'SMTPLIB' MODULE
        elif'email to rohit' in query:
            try:
                speak('What should i say')
                content=takeCommand() #This function is converting human voice into text message
                to='rohitsingh38347@gmail.com' #Email ID on which email will get send
                sendEmail(to,content) 
                speak('Email has been sent')
            
            #We are rasing exception so that if any exception occur then the jarvis will not misbehave
            except Exception as e:
                print(e)
                speak('ooops! Try again')




        

