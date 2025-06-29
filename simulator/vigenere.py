def vigenere_encrypt(text, key):
    key = key.lower()
    encrypted_text = []
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('a')
            if char.islower():
                encrypted_text.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            else:
                encrypted_text.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
            key_index = (key_index + 1) % len(key)
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def vigenere_decrypt(text, key):
    key = key.lower()
    decrypted_text = []
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('a')
            if char.islower():
                decrypted_text.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
            else:
                decrypted_text.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
            key_index = (key_index + 1) % len(key)
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

password = "key"
plaintext = "This is a test message."

encrypted = vigenere_encrypt(plaintext, password)
print(f"Encrypted: {encrypted}")

decrypted = vigenere_decrypt(encrypted, password)
print(f"Decrypted: {decrypted}")
