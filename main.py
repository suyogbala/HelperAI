import os
import speech_recognition as sr
import webbrowser
import datetime
import openai

def ai(prompt):
    openai.api_key = "Your key"
    word = f'OpenAI Response for: {prompt}'
    response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prompt,
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    word += response["choices"][0]["text"]
    if not os.path.exists("/Users/suyogbala/Documents/codinglanguages/python.py/DeskAssistant/Answers"):
        os.mkdir("/Users/suyogbala/Documents/codinglanguages/python.py/DeskAssistant/Answers")
    
    with open(f"/Users/suyogbala/Documents/codinglanguages/python.py/DeskAssistant/Answers/{''.join(prompt.split('helper')[1:]).strip()}.txt", "w") as f:
        f.write(word)

def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    print("Checking microphone permissions...")

    with sr.Microphone() as source:
        print('Listening...')
        r.adjust_for_ambient_noise(source)  
        audio = r.listen(source)
        print('Processing...')

        try:
            query = r.recognize_google(audio, language='en-US')
            print(f'User Said: {query}')
            return query

        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        
        except sr.RequestError:
            return "Sorry, I'm having trouble accessing the service."

if __name__ == '__main__':
    say("Hello, I am your helper AI.")
    while True:
        query = takeCommand().lower()
        print('You said:', query)

        if 'helper'.lower() in query.lower():
            ai(prompt = query)

        elif 'time' in query:
            time_now = datetime.datetime.now().strftime("%I:%M %p")
            say(f'The time is {time_now}')

        elif 'facetime' in query:
            path = '/System/Applications/FaceTime.app'
            os.system(f'open {path}')
        
        else:   
            sites = {'youtube': "https://www.youtube.com", 'wikipedia': "https://www.wikipedia.com", 'google': "https://www.google.com"}
            for keyword, site in sites.items():
                if keyword in query:
                    say(f'Opening {keyword}')
                    webbrowser.open(site)

        if 'quit' in query.lower():
            exit()


        