alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]
exit = False

#     shifted_index = 0
#     for letter in orignial_text:
#         original_index = alphabet.index(letter)
#         shifted_index = original_index + shift_amount
#         if shifted_index >= len(alphabet):
#             shifted_index = shifted_index - len(alphabet)
#             shifted_word += alphabet[shifted_index]
#         else:
#             shifted_word += alphabet[shifted_index]


#     print(shifted_word)
def encrypt(orignial_text, shift_amount):
    shifted_word = ""
    for letter in orignial_text:
        if letter not in alphabet:
            shifted_word += letter
            continue
        shifted_index = alphabet.index(letter) + shift_amount
        shifted_index %= len(alphabet)
        shifted_word += alphabet[shifted_index]
    print(shifted_word)


def decrypt(cipher_text, shift_amount):
    shifted_word = ""
    for letter in cipher_text:
        if letter not in alphabet:
            shifted_word += letter
            continue
        shifted_index = alphabet.index(letter) - shift_amount
        shifted_index %= len(alphabet)
        shifted_word += alphabet[shifted_index]
    print(shifted_word)


def caesar(direction):
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)


while not exit:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction)
    answer = input("Continue y/n\n")
    if answer.lower() == "n":
        exit = True
    else:
        exit = False
