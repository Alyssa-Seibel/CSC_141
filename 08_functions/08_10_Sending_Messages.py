
sent_messages = []   
messages = ['hi','how are you','what are you doing']
def send_messages(messages):
    while messages:
        current = messages.pop()
        print(f"Sending: {current}...")
        sent_messages.append(current)

send_messages(messages)       
print('\nThe following messages have been sent:')
for sent in sent_messages:
    print(sent)    

