#task1 of my internship
print('''
      

░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝
''')

def myfirst_chatbot():
    print("Hello! I'm your friendly chatbot. How can I help you today?")

    while True:
        user_input = input("You: ").lower()  # Convert input to lowercase for consistency

        if 'hello' in user_input or 'hi' in user_input:
            print("Chatbot: Hi there! How can I assist you today?")
        elif 'how are you' in user_input:
            print("Chatbot: I'm just a bot, but I'm doing great! How can I help?")
        elif 'bye' in user_input or 'goodbye' in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break  # Exit the loop and end the chat
        elif 'can you please tell your name' in user_input:
            print("Chatbot: I don't have a name, but you can call me Chatbot.")
        elif 'how is weather today' in user_input:
            print("Chatbot: I don't have access to weather data, but you can check a weather app!")
        else:
            print("Chatbot: I'm not sure how to respond to that. Can you ask something else?")


myfirst_chatbot()
