# chatbot.py



# Import necessary libraries

import nltk                      # Natural Language Toolkit for NLP tasks

import re                        # Regular expression module for pattern matching

import random                    # For selecting random responses



# Import specific components from NLTK

from nltk.stem import WordNetLemmatizer  # Used to reduce words to their base form (lemmatization)

from nltk.corpus import stopwords        # Contains a list of common "stop words" like 'the', 'is', 'a'



# --- NLTK Data Downloads ---

# These 'try-except' blocks ensure that the necessary NLTK data models are downloaded.

# They are crucial for the lemmatizer, tokenizer, and stopwords functionality.

# You only need to run these downloads once.



# Download WordNet: A lexical database for English, used by the lemmatizer.

try:

    nltk.data.find('corpora/wordnet')

except LookupError:

    print("Downloading 'wordnet' NLTK data...")

    nltk.download('wordnet')

    print("Download complete.")



# Download 'punkt' tokenizer data: Essential for `nltk.word_tokenize`.

# The traceback explicitly requested 'punkt_tab', so we're attempting to download that directly.

try:

    # Check for the general 'punkt' corpus. If not found, download 'punkt_tab'.

    nltk.data.find('corpora/punkt')

except LookupError:

    print("Downloading 'punkt_tab' NLTK data for tokenizer...")

    # Explicitly downloading 'punkt_tab' as suggested by the traceback.

    nltk.download('punkt_tab')

    print("Download complete.")



# Download 'stopwords': A list of common English stop words.

try:

    nltk.data.find('corpora/stopwords')

except LookupError:

    print("Downloading 'stopwords' NLTK data...")

    nltk.download('stopwords')

    print("Download complete.")



# Initialize the WordNet Lemmatizer.

# This object will be used to lemmatize words in the user's input.

lemmatizer = WordNetLemmatizer()



# Define common stop words in English.

# These words are usually filtered out as they don't carry much meaning for simple rule-based matching.

stop_words = set(stopwords.words('english'))



# --- Knowledge Base / Chatbot Rules ---

# This is the core "brain" of our simple chatbot.

# It's a list of dictionaries, where each dictionary represents a conversation rule.

# Each rule has:

#   - 'patterns': A list of regular expressions that the chatbot will try to match against the user's input.

#                 If any pattern matches, the rule is triggered.

#   - 'responses': A list of possible responses. When a rule is triggered, one response is chosen randomly.

rules = [

    {

        'patterns': [r'hi|hello|hey|greetings'], # Patterns for greetings

        'responses': ["Hello! How can I help you today?", "Hi there!", "Hey! What's up?"]

    },

    {

        'patterns': [r'how are you', r'how do you do'], # Patterns for asking about the chatbot's well-being

        'responses': ["I'm just a program, but I'm doing great!", "I'm functioning perfectly, thanks for asking!", "I'm an AI, so I don't have feelings, but I'm ready to assist!"]

    },

    {

        'patterns': [r'your name', r'who are you'], # Patterns for asking about the chatbot's identity

        'responses': ["I am a simple AI chatbot.", "You can call me ChatBot.", "I don't have a name, but I'm here to chat!"]

    },

    {

        'patterns': [r'what can you do', r'help me', r'capabilities'], # Patterns for inquiring about chatbot functions

        'responses': ["I can answer simple questions and engage in basic conversation.", "I'm here to assist with your queries!", "Ask me anything! I'll do my best to help."]

    },

    {

        'patterns': [r'bye|goodbye|see you'], # Patterns for farewells

        'responses': ["Goodbye! Have a great day!", "See you later!", "Bye for now!"]

    },

    {

        'patterns': [r'thank you|thanks'], # Patterns for expressions of gratitude

        'responses': ["You're welcome!", "No problem!", "Glad I could help!"]

    },

    {

        'patterns': [r'weather', r'temperature'], # Patterns for weather inquiries

        'responses': ["I cannot access real-time weather data. I am just a simple chatbot.", "Sorry, I don't have information about the weather."]

    },

    {

        'patterns': [r'time'], # Patterns for time inquiries

        'responses': ["I cannot tell the current time accurately as I don't have real-time clock access. My responses are pre-programmed.", "My apologies, I can't provide the exact time."]

    },

    {

        'patterns': [r'joke', r'funny'], # Patterns for requesting a joke

        'responses': ["Why don't scientists trust atoms? Because they make up everything!", "What do you call a fish with no eyes? Fsh!", "Parallel lines have so much in common. It's a shame they'll never meet."]

    },

    {

        'patterns': [r'favorite color'], # Patterns for asking about favorite color

        'responses': ["I don't have a favorite color, but I find the color of code quite beautiful!", "As an AI, I don't perceive colors."]

    },

    {

        'patterns': [r'tell me about (.*)', r'what is (.*)'], # Patterns with a capturing group `(.*)`

        # The `(.*)` captures any text after "tell me about" or "what is".

        # This captured text is then substituted into the response using `{0}`.

        'responses': ["I can try to tell you about {0}.", "What specifically about {0} would you like to know?", "That's an interesting topic! What about {0}?"]

    }

]



# --- NLP Processing Functions ---



def preprocess_input(text):

    """

    Cleans and processes the input text for better matching.

    Steps include:

    1. Converting text to lowercase.

    2. Tokenizing the text into individual words.

    3. Removing non-alphabetic tokens and common stop words.

    4. Lemmatizing the remaining words to their base form.

    

    Args:

        text (str): The raw user input string.

        

    Returns:

        str: The processed text string, ready for pattern matching.

    """

    text = text.lower()  # Convert input to lowercase to ensure case-insensitive matching

    

    # Tokenize the text into individual words (e.g., "Hello, world!" -> ["Hello", ",", "world", "!"])

    tokens = nltk.word_tokenize(text) 

    

    # Process tokens:

    #   - `word.isalpha()`: Keeps only tokens that are purely alphabetic (removes punctuation, numbers).

    #   - `word not in stop_words`: Filters out common words like "the", "is", "a".

    #   - `lemmatizer.lemmatize(word)`: Reduces words to their dictionary root form (e.g., "running" -> "run").

    processed_tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalpha() and word not in stop_words]

    

    # Join the processed tokens back into a single string, separated by spaces, for regex matching.

    return " ".join(processed_tokens)



def get_response(user_input):

    """

    Determines the chatbot's response based on the user's input.

    It preprocesses the input and then checks it against the defined rules.

    

    Args:

        user_input (str): The raw string input from the user.

        

    Returns:

        str: The chatbot's chosen response, or a default message if no match is found.

    """

    # First, preprocess the user's input to clean and normalize it.

    processed_input = preprocess_input(user_input)



    # Iterate through each rule defined in our 'rules' knowledge base.

    for rule in rules:

        # For each rule, iterate through all its defined patterns.

        for pattern in rule['patterns']:

            # Attempt to find a match for the current pattern in the processed user input.

            match = re.search(pattern, processed_input)

            

            # If a match is found:

            if match:

                # Check if the pattern used capturing groups (e.g., `(.*)`).

                if match.groups():

                    # If capturing groups exist, format the response by substituting the captured text.

                    # `random.choice(rule['responses'])` picks one response randomly.

                    # `.format(*match.groups())` inserts the captured text into placeholders like `{0}`.

                    response = random.choice(rule['responses']).format(*match.groups())

                else:

                    # If no capturing groups, just pick a random response from the rule's list.

                    response = random.choice(rule['responses'])

                

                # Return the chosen response immediately once a match is found.

                return response

    

    # If the loop completes and no matching rule is found, return a default "I don't understand" message.

    return "I'm not sure how to respond to that. Can you rephrase or ask something else?"



# --- Chatbot Main Loop ---



def run_chatbot():

    """

    The main function that runs the interactive chatbot session.

    It continuously prompts the user for input and provides responses until the user decides to exit.

    """

    print("AI Chatbot: Hello! I'm a simple chatbot. Type 'bye' to exit.")

    print("-" * 50) # Print a separator line for better readability



    # Start an infinite loop for continuous conversation.

    while True:

        user_input = input("You: ") # Get input from the user.

        

        # Check if the user wants to exit the chat.

        # `.lower()` converts input to lowercase for case-insensitive checking.

        if user_input.lower() in ['bye', 'goodbye', 'exit', 'quit']:

            # If exiting, print a random farewell message and break the loop.

            print("AI Chatbot:", random.choice(["Goodbye! Have a great day!", "See you later!", "Bye for now!"]))

            break

        

        # Get the chatbot's response based on the user's input.

        response = get_response(user_input)

        

        # Print the chatbot's response.

        print("AI Chatbot:", response)

        print("-" * 50) # Print another separator line.



# --- Entry Point of the Script ---

# This ensures that `run_chatbot()` is called only when the script is executed directly,

# not when it's imported as a module into another script.

if __name__ == "__main__":

    run_chatbot()
