alphabets = ['a','b','c','d','e','f','g','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plane_text,shift_key):
    cipher_text = ''
    for char in plane_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position + shift_key)%26
            cipher_text += alphabets[new_position]
        else:
            cipher_text += char

        print(f'Here is the text after encryption: {cipher_text} ')

def decryption(cipher_text,shift_key):
    plane_text = ''
    for char in cipher_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position - shift_key)%26
            plane_text += alphabets[new_position]
        else:
            plane_text += char
        
        
        print(f'Here is the text after encryption: {plane_text} ')


ending = False
while not ending:
    work = input("Enter encrypt for encryption decrypt for discryption: ")

    alpha = input("Text your message: ")

    shift = int(input("Enter shift_key: "))

    if work == "encrypt":
        encryption(plane_text = alpha,shift_key = shift)
    elif work == "decrypt":
        decryption(cipher_text = alpha,shift_key = shift)

    iteration = input("Enter yes to continue and no to exit.")

    if iteration == "no":
        ending = True
        print("Good bye have a fucking nice day: ")