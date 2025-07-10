def rulebased_chatbot():
    print("Hi! I am a basic chatbot. Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "quit":
            print("Chatbot: Goodbye! Have a great day.")
            break

        # Greeting
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you?")

        # Asking for help
        elif "help" in user_input:
            print("Chatbot: Sure, I am here to assist you.")

        # Asking about creator
        elif "who created you" in user_input or "your creator" in user_input:
            print("Chatbot: I was created by Eng. Diya Banerjee.")

        # Asking about name
        elif "your name" in user_input:
            print("Chatbot: My name is AI Robot.")

        # Asking how are you
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bunch of code, but I'm doing great!")

        # Asking about weather
        elif "weather" in user_input or "raining" in user_input:
            print("Chatbot: I can't check live weather, but it seems sunny!")

        # Default response
        else:
            print("Chatbot: I'm not sure how to respond to that.")

# Run the chatbot
rulebased_chatbot()
