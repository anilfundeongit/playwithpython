import cipher_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
user_choice = ''

print(cipher_art.logo)

def caesor(original_text, shift_number):
    display_string = ''
    for letter in original_text:
        if direction == 'decode':
            if letter not in alphabet:
                display_string = display_string + letter
            else:
                display_string = display_string + alphabet[alphabet.index(letter) - shift_number]
        else:
            if letter not in alphabet:
                display_string = display_string + letter
            elif alphabet.index(letter) + shift_number > 25:
                display_string = display_string + alphabet[(alphabet.index(letter) + shift_number) % 2]
            else:
                display_string = display_string + alphabet[alphabet.index(letter) + shift_number]

    print(display_string)

def encrypt(original_text, shift_number):
    display_string = ''
    for letter in original_text:
        if alphabet.index(letter) + shift_number > 25:
            display_string = display_string + alphabet[(alphabet.index(letter) + shift_number) % 2]
        else:
            display_string = display_string + alphabet[alphabet.index(letter) + shift_number]

    print(display_string)


def decrypt(original_text, shift_number):
    display_string = ''
    for letter in original_text:
        display_string = display_string + alphabet[alphabet.index(letter) - shift_number]

    print(display_string)

while user_choice != 'no':

    direction = input("Type 'encode' to encrypt , type 'decode' to  decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesor(original_text=text, shift_number=shift)
    user_choice = input('Do you want to continue with program?').lower()







