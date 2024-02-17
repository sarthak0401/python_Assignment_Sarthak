import nltk
from nltk.chat.util import Chat, reflections

pattern = [
    (r'hello', ['Hello!', 'Hey there!', 'Hi!']),
    (r'quit', ['Bye! Take care.', 'Goodbye, have a nice day!', 'See you later.']),
    (r'how are you', ['I am great, thanks for asking!'])
]

Buddy = Chat(pattern, reflections)

print("Welcome to the Chatbot. Type 'quit' to exit.")
while True:
    input_by_user = input("You: ")
    response = Buddy.respond(input_by_user)
    print("Chatbot:", response)
    if input_by_user.lower() == 'quit':
        break
