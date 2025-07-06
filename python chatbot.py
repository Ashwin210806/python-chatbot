print("Hi! I'm a simple chatbot.")
print("You can say: hello, bye, joke, weather, or help")
print("Type 'quit' to stop talking to me.")
print()

while True:

    user_message = input("You: ")
    
    if user_message == "quit":
        print("Bot: Goodbye!")
        break
    
    elif user_message == "hello" or user_message == "hi":
        print("Bot: Hello! Nice to meet you!")
    
    elif user_message == "bye":
        print("Bot: Bye! Have a good day!")
    
    elif user_message == "joke":
        print("Bot: Why did the chicken cross the road? To get to the other side!")
    
    elif user_message == "weather":
        print("Bot: I hope it's sunny today!")
    
    elif user_message == "help":
        print("Bot: You can say: hello, bye, joke, weather, or help")
    
    elif user_message == "how are you":
        print("Bot: I'm good! Thanks for asking!")
    
    elif user_message == "what is your name":
        print("Bot: My name is SimpleBot!")
    
    else:
        print("Bot: I don't understand. Try saying: hello, bye, joke, weather, or help")