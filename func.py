def encrypt(text: str, shift: int):
    """Encrypt the message using Cesar's encrypter basis alphabet list."""
    alphabet = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ ")
    result = []

    for char in text:

        if char.upper() in alphabet:
            char = char.upper()
            # Calculate the position in the alphabet and change to "new letter" after shift
            original_index = alphabet.index(char)
            new_index = (original_index + shift) % len(alphabet)
            new_char = alphabet[new_index]
            result.append(new_char)
        

        else:
            result.append(char)

    return ''.join(result)