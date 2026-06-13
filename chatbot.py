def basic_chatbot():
    print("--- Welcome to the Basic Chatbot ---")
    print("Type 'bye' to exit the chat.\n")

    # Loop to keep the conversation going
    while True:
        # Get user input and convert to lowercase for easier matching
        user_input = input("You: ").strip().lower()

        # Rule-based responses using if-elif
        if user_input == "hello":
            print("Bot: Hi!")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break  # Exits the loop
        else:
            print("Bot: I'm a simple bot. Try saying 'hello', 'how are you', or 'bye'.")

if __name__ == "__main__":
    basic_chatbot()
