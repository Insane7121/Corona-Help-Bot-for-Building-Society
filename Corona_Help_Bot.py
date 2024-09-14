import smtplib
import webbrowser

import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

# Function to make the bot speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to take a voice command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Could not understand your command. Please say that again...")
        return "none"
    return query.lower()

# Function to send an email alert (requires configuration)
def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('your_email@gmail.com', 'your_password')
        server.sendmail('your_email@gmail.com', to, content)
        server.close()
        speak("Email has been sent successfully!")
    except Exception as e:
        print(e)
        speak("Sorry, I am not able to send the email right now.")

# Function to send SMS using Twilio (requires setup)
def sendSMS(body):
    from twilio.rest import Client

    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=body,
        from_='+1234567890',  # Twilio phone number
        to='+919876543210'  # Recipient's phone number
    )

    speak("SMS has been sent!")

# Main function that listens to commands and acts
def main():
    speak("Hello, I am the Corona Help Bot for your building society. How may I assist you today?")

    while True:
        query = takeCommand()

        if 'symptoms' in query:
            speak("Common symptoms of COVID-19 include fever, dry cough, and tiredness. Less common symptoms are sore throat, headache, loss of taste or smell, and difficulty breathing.")
        
        elif 'prevention' in query:
            speak("To prevent the spread of COVID-19, wear a mask, wash your hands frequently with soap and water, maintain social distancing, and avoid touching your face.")
        
        elif 'hospital' in query:
            speak("Opening a list of nearby hospitals...")
            webbrowser.open("https://www.google.com/search?q=nearby+hospitals")
        
        elif 'vaccine' in query:
            speak("You can check the availability of COVID-19 vaccines on the CoWIN platform.")
            webbrowser.open("https://www.cowin.gov.in/")

        elif 'send email' in query:
            speak("What should the email say?")
            content = takeCommand()
            to = "recipient_email@gmail.com"  # Replace with the recipient's email
            sendEmail(to, content)

        elif 'send sms' in query:
            speak("What should the SMS say?")
            sms_content = takeCommand()
            sendSMS(sms_content)

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye! Stay safe.")
            break

if __name__ == "__main__":
    main()
