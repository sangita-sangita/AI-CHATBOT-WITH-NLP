# AI-CHATBOT-WITH-NLP

COMPANY NAME:CODTECH IT SOLUTIONS
NAME : SANGITA KUMARI
INTERN ID: 
DOMAIN:PYTHON PROGRAMMING
DURATION:6 WEEKS
MENTOR:NEELA SANTOSH



Simple AI Chatbot

This project is a rule-based AI chatbot built in Python using the Natural Language Toolkit (NLTK). It’s designed to engage users in basic text-based conversations using pre-defined patterns and responses. The chatbot demonstrates foundational natural language processing (NLP) techniques like tokenization, lemmatization, stopword removal, and regular expression matching.

📌 Features
* Rule-based conversation system using regular expressions

* Text preprocessing (lowercasing, stopword removal, lemmatization)

* Dynamic responses using captured phrases (e.g., "Tell me about X")

* Fallback response when no rules match

* Simple interactive loop in the terminal

🔧 How It Works
* Input Processing:
User input is converted to lowercase, tokenized, cleaned of punctuation and stop words, and then lemmatized using WordNet.

* Pattern Matching:
A set of predefined rules (patterns + responses) is used to match against processed input. If a match is found, a random response is selected from the rule.

* Capturing Groups:
Some rules use capturing groups (like what is (.*)) to extract parts of the input and dynamically insert them into the response.

* Fallback Handling:
If no match is found, the chatbot replies with a default "I don't understand" message.

🧱 Dependencies
Python 3.x

* NLTK (Natural Language Toolkit)

* To install NLTK:

* bash
Copy code
pip install nltk
Required NLTK datasets (automatically downloaded if not present):

* wordnet

* punkt

* stopwords

▶️ Usage
Run the chatbot script from your terminal:

bash
Copy code
python chatbot.py
You'll see a prompt like:

markdown
Copy code
AI Chatbot: Hello! I'm a simple chatbot. Type 'bye' to exit.
--------------------------------------------------
You:
Type your message and interact with the chatbot. To exit, type bye, exit, quit, or goodbye.

📚 Example Conversations
vbnet
Copy code
You: Hello
AI Chatbot: Hi there!

You: What is Python?
AI Chatbot: I can try to tell you about Python.

You: Tell me a joke
AI Chatbot: Why don't scientists trust atoms? Because they make up everything!

You: Thanks
AI Chatbot: You're welcome!
📂 File Structure
bash
Copy code
chatbot.py         # Main script with chatbot logic and rules
README.md          # Project documentation
🧠 Customization
* You can add more conversational rules by modifying the rules list in chatbot.py. Each rule is a dictionary with:

* patterns: list of regex patterns to match user input

* responses: list of potential replies to choose from

Example:

python
Copy code
{
    'patterns': [r'who created you'],
    'responses': ["I was created by a Python developer!", "Just some code and logic brought me to life."]
}
⚠️ Limitations
Cannot fetch real-time data (e.g., weather, current time)

Rule-based — doesn’t learn or understand context

Relies heavily on pattern matching and may misinterpret inputs

📘 License
This project is provided for educational purposes. Feel free to modify and expand it for your own chatbot experiments.

Let me know if you'd like a more technical or beginner-friendly version!
