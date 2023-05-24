import random

# Define the chatbot responses
greetings = ['Hello!', 'Hi!', 'Hey there!', 'Greetings!', 'Nice to see you!']
goodbyes = ['Goodbye!', 'See you later!', 'Farewell!', 'Bye!', 'Take care!']
help_responses = ['How may I assist you?', 'What can I do for you?', 'How can I help?']
problem_responses = ['I\'m sorry to hear that. Can you please tell me more about the problem?', 'Let me see if I can help. What seems to be the issue?', 'I\'ll do my best to help you. What\'s the problem?']
thankyou_responses = ['You are welcome!', 'No problem!', 'It was my pleasure!', 'Glad to help!']

# Define the chatbot function
def chatbot():
    print('Chatbot: ' + random.choice(greetings))
    while True:
        user_input = input('User: ').lower()
        if 'hello' in user_input or 'hi' in user_input or 'hey' in user_input:
            print('Chatbot: ' + random.choice(greetings))
        elif 'bye' in user_input or 'goodbye' in user_input or 'see you' in user_input:
            print('Chatbot: ' + random.choice(goodbyes))
            break
        elif 'help' in user_input or 'support' in user_input:
            print('Chatbot: ' + random.choice(help_responses))
        elif 'problem' in user_input or 'issue' in user_input or 'error' in user_input:
            print('Chatbot: ' + random.choice(problem_responses))
        elif 'thank you' in user_input or 'thanks' in user_input or 'thankyou' in user_input:
            print('Chatbot: ' + random.choice(thankyou_responses))
        else:
            print('Chatbot: I\'m sorry, I don\'t understand. Can you please rephrase your request?')

# Test the chatbot
chatbot()


#alternavtive using dictionary

# import random

# # Define the chatbot responses
# responses = {
#     'greetings': ['Hello!', 'Hi!', 'Hey there!', 'Greetings!', 'Nice to see you!'],
#     'goodbyes': ['Goodbye!', 'See you later!', 'Farewell!', 'Bye!', 'Take care!'],
#     'help': ['How may I assist you?', 'What can I do for you?', 'How can I help?'],
#     'problem': ['I\'m sorry to hear that. Can you please tell me more about the problem?',
#                 'Let me see if I can help. What seems to be the issue?',
#                 'I\'ll do my best to help you. What\'s the problem?'],
#     'thankyou': ['You are welcome!', 'No problem!', 'It was my pleasure!', 'Glad to help!']
# }

# # Define the chatbot function
# def chatbot():
#     print('Chatbot: ' + random.choice(responses['greetings']))
#     while True:
#         user_input = input('User: ')
#         if any(word in user_input for word in ['hello', 'hi', 'hey']):
#             print('Chatbot: ' + random.choice(responses['greetings']))
#         elif any(word in user_input for word in ['bye', 'goodbye', 'see you']):
#             print('Chatbot: ' + random.choice(responses['goodbyes']))
#             break
#         elif any(word in user_input for word in ['help', 'support']):
#             print('Chatbot: ' + random.choice(responses['help']))
#         elif any(word in user_input for word in ['problem', 'issue', 'error']):
#             print('Chatbot: ' + random.choice(responses['problem']))
#         elif any(word in user_input for word in ['thank you', 'thanks', 'thankyou']):
#             print('Chatbot: ' + random.choice(responses['thankyou']))
#         else:
#             print('Chatbot: I\'m sorry, I don\'t understand. Can you please rephrase your request?')

# # Test the chatbot
# chatbot()
