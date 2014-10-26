'''
secretCode.py

This is a way to encode and decode secret messages to your friends.

author: sabadam32
'''

method = input("Do you want to encode a secret message[y/n]: ")
if method.lower()[0:1] =='y':
    message = input("Enter the message to encode")
    message = [chr(ord(x)+3) for x in message]
    print(''.join(message))
else:
    message = input("OK then enter the message to decode: ")
    message = [chr(ord(x)-3) for x in message]
    print(''.join(message))
    
