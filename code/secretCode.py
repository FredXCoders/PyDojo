'''
secretCode.py

Implementation of a caesar cipher.

author: sabadam32
'''

# Get a list of the uppercase letters and refer to it as ascii
from string import ascii_uppercase as ascii

method = raw_input("Do you want to encode a secret message[y/n]: ")

# The key is a number that shifts all the letters around
key = int(raw_input("Enter a number between 1 and 25 for key: "))

# Now we take all the letters and shift them by the number of spaces set by the key
# if the key is 2 then A would become Y, B would become Z.  After Z the letters start from A again
# so C would become A, D would become B and so on. 
shifted_letters = ascii[-key:]+ascii[:-key]

# Make sure we keep the spaces
letter_mapping= {' ':' '}

if method.lower()[0:1] =='y':

    # We are now going to go through all the letters and assign it's new value in the letter_mapping object
    # We use the list of letters we already have in the ascii variable and assign its new value from
    # the shifted letters we have in the letters variable.
    for x, y in enumerate(ascii):
        letter_mapping[y] = shifted_letters[x]

    message = raw_input("Enter the message to encode: ")

    # Now that we have the mapping of real letters to shifted letters we can encode our message
    # This is a tricky statement that basically takes all the letters in the message, converts them
    # to uppercase letters and then looks up that letters new value in the letter mapping variable.
    # We then re-assign the encoded message to the message variable.
    message = [letter_mapping[x] for x in message.upper()]
else:

    # We are now going to go through all the letters and assign it's new value in the letter_mapping object
    # We use the list of shifted letters we already have in the shifted_letters variable and assign its new value from
    # the normal letters we already have in the letters variable.
    for x, y in enumerate(ascii):
        letter_mapping[shifted_letters[x]] = y

    message = raw_input("OK then enter the message to decode: ")

    # Now that we have the mapping of shifted letters back to normal letters we can decode our message
    # This is a tricky statement that basically takes all the letters in the message, converts them
    # to uppercase letters and then looks up that letters new value in the letter mapping variable.
    # We then re-assign the decoded message to the message variable.
    message = [letter_mapping[x] for x in message.upper()]

# Now that message contains what we want we will print it o the screen
print(''.join(message))
