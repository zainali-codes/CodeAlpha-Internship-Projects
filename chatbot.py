print("🤖 ChatBot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("🤖 ChatBot: Goodbye! 👋")
        break

    elif "hello" in user_input or "hi" in user_input:
        print("🤖 ChatBot: Hello! How can I help you?")

    elif "how are you" in user_input:
        print("🤖 ChatBot: I'm fine! Thanks for asking 😊")

    elif "your name" in user_input:
        print("🤖 ChatBot: I am a simple Python chatbot 🤖")

    elif "help" in user_input:
        print("🤖 ChatBot: I can chat with you! Try saying hello 👀")

    else:
        print("🤖 ChatBot: Sorry, I don't understand that 😅")