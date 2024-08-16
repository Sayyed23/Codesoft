import wikipedia
import pyjokes
import webbrowser
import datetime
import time
import requests

# Function to wish the user based on the time of day
def wish():
    hour = datetime.datetime.now().hour
    tt = time.strftime("%I:%M %p") 
    if hour >= 0 and hour < 12:
        return f"Good morning, it's {tt}"
    elif hour >= 12 and hour < 18:
        return f"Good afternoon, it's {tt}"
    else:
        return f"Good evening, it's {tt}"

# Function to fetch a story from Wikipedia
def get_wikipedia_story(topic):
    try:
        summary = wikipedia.summary(topic, sentences=5)  # Fetch a summary of up to 5 sentences
        return summary
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find a story on that topic."
    except wikipedia.exceptions.DisambiguationError as e:
        return f"That topic is ambiguous. Here are some suggestions: {e.options}"

# Function to tell a random joke using pyjokes
def get_random_joke():
    joke = pyjokes.get_joke()
    return joke

# Function to get the current time
def get_current_time():
    return time.strftime("%I:%M %p")

# Function to get the current date
def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

# Function to fetch a random fact from an API
def get_random_fact():
    try:
        response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
        fact = response.json().get('text', 'No fact available.')
        return fact
    except Exception as e:
        return f"An error occurred: {e}"

# Function to perform basic arithmetic calculations
def simple_calculator(expression):
    try:
        result = eval(expression)
        return f"The result is: {result}"
    except Exception as e:
        return f"Error: {e}"

# Function to convert temperature units
def convert_temperature(value, unit_from, unit_to):
    try:
        value = float(value)
        if unit_from == 'celsius' and unit_to == 'fahrenheit':
            return (value * 9/5) + 32
        elif unit_from == 'fahrenheit' and unit_to == 'celsius':
            return (value - 32) * 5/9
        else:
            return "Unsupported conversion."
    except Exception as e:
        return f"Error: {e}"

# Function to fetch dictionary definition
def get_definition(word):
    try:
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        data = response.json()
        meanings = data[0]['meanings'][0]['definitions']
        definitions = [meaning['definition'] for meaning in meanings]
        return "\n".join(definitions)
    except Exception as e:
        return f"An error occurred: {e}"

# Enhanced Chatbot using if-else statements and Wikipedia API
def chatbot():
    print(wish())  # Greet the user based on the time of day
    print("Hello! I'm a simple chatbot. How can I help you today?")
    
    while True:
        query = input("You: ").lower()

        if "hello" in query or "hi" in query:
            print("Chatbot: Hello! How can I assist you?")
        elif "how are you" in query:
            print("Chatbot: I'm just a program, so I don't have feelings, but thanks for asking!")
        elif "your name" in query:
            print("Chatbot: I'm a simple rule-based chatbot.")
        elif "what can you do" in query:
            print("Chatbot: I can respond to simple questions, tell you a joke, fetch information from Wikipedia, give you the current time, date, random facts, perform calculations, convert units, and provide dictionary definitions!")
        elif "tell me a joke" in query:
            print(f"Chatbot: {get_random_joke()}")
        elif "current time" in query:
            print(f"Chatbot: The current time is {get_current_time()}.")
        elif "current date" in query:
            print(f"Chatbot: Today's date is {get_current_date()}.")
        elif "random fact" in query:
            print(f"Chatbot: {get_random_fact()}")
        elif "calculate" in query:
            expression = input("Chatbot: Please provide the expression to calculate (e.g., 5 + 3): ")
            print(f"Chatbot: {simple_calculator(expression)}")
        elif "convert temperature" in query:
            value = input("Chatbot: Please provide the temperature value: ")
            unit_from = input("Chatbot: From which unit (celsius or fahrenheit)? ").lower()
            unit_to = input("Chatbot: To which unit (celsius or fahrenheit)? ").lower()
            result = convert_temperature(value, unit_from, unit_to)
            print(f"Chatbot: The converted temperature is {result}.")
        elif "define" in query:
            word = query.replace("define", "").strip()
            if word:
                print(f"Chatbot: Here is the definition of {word}:")
                print(get_definition(word))
            else:
                print("Chatbot: Please specify a word to define.")
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
        elif "open facebook" in query:
            webbrowser.open("https://www.facebook.com")
        elif "open instagram" in query:
            webbrowser.open("https://www.instagram.com")
        elif "open google" in query:
            search_query = input("Chatbot: Sir, what should I search on Google? ").strip()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
        elif "tell me a story" in query:
            print("Chatbot: Sure! What story would you like to hear?")
            story_topic = input("You: ").strip()
            if story_topic:
                print(f"Chatbot: Let me tell you a story about {story_topic}...")
                story = get_wikipedia_story(story_topic)
                print(f"Chatbot (Story): {story}")
            else:
                print("Chatbot: Please specify a topic for the story.")
        elif "wikipedia" in query:
            topic = query.replace("wikipedia", "").strip()
            if topic:
                print("Chatbot: Let me look that up for you...")
                summary = get_wikipedia_story(topic)
                print(f"Chatbot (Wikipedia): {summary}")
            else:
                print("Chatbot: Please specify a topic to search on Wikipedia.")
        elif "bye" in query or "exit" in query:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you please ask something else?")

# Run the chatbot
chatbot()
