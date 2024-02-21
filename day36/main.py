
morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
              'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '0': '------', '1': '.-----', '2': '..---', '3': '...--', '4': '....-',
              '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
              '-': '-....-', '?': '..--..', '/': '-..-.', ';': '-.-.-.', ':': '--..--', '"': '.-..-.', "'": '.----.',
              ' ': '/'}


# ---------------------------- ENCODER ------------------------------- #
def encode_message(message):
    try:
        encoded_message = [morse_dict[char] for char in message]
    except KeyError:
        print("Sorry, only punctuation used to construct sentences.  eg '.', ',', '-', '?', '/', ';', ':', ''', '''' ")
    else:
        print(*encoded_message, sep=' ')


# ---------------------------- DECODER ------------------------------- #
def decode_message(message):

    message_char = message.split()

    decoded_message = []
    try:
        for char in message_char:
            key_list = list(morse_dict.keys())
            val_list = list(morse_dict.values())

            position = val_list.index(char)
            decoded_message.append(key_list[position])
    except ValueError:
        print("Sorry error in your message!")
    else:
        print(*decoded_message, sep=' ')


converter_on = True

while converter_on:
    message = input("Enter message in Morse Code converter: ").upper()
    if message == 'EXIT':
        converter_on = False
    else:
        function = input("Enter 'encode' or 'decode' message: ")

        if function == 'encode':
            encode_message(message)
        elif function == 'decode':
            decode_message(message)


