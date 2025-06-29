# DISCLAIMER
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#   SOFTWARE.


import chardet  # Library to detect file encoding (install using pip if needed)
import os
import time

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


def EncryptFile(file, password):
    # Detect file encoding
    with open(file, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']

    if not encoding:  # If encoding can't be detected, assume binary
        print(f"Skipping binary file: {file}")
        return

    # Read and encrypt the file content
    with open(file, 'r', encoding=encoding, errors='ignore') as f:
        plaintext = f.read()

    encrypted_text = vigenere_encrypt(plaintext, password)

    # Save encrypted content and delete original file
    with open(file + ".vigenere", 'w', encoding='utf-8') as f:
        f.write(encrypted_text)
    os.remove(file)


def DecryptFile(file, password):
    try:
        # Read and decrypt the file content
        with open(file, 'r', encoding='utf-8') as f:
            encrypted_text = f.read()

        decrypted_text = vigenere_decrypt(encrypted_text, password)

        # Save decrypted content and delete encrypted file
        with open(file.split(".vigenere")[0], 'w', encoding='utf-8') as f:
            f.write(decrypted_text)
        os.remove(file)
    except Exception as e:
        print(f"File {file} cannot be decrypted! Error: {e}")

def EncryptDir(directory, password) -> int:
    count = 0
    for dirpath, _dirnames, filenames in os.walk(directory, topdown=False):
        for name in filenames:
            EncryptFile(os.path.join(dirpath, name), password)
            count += 1
        time.sleep(0.01)  # sleep 10 milliseconds
    return count

def DecryptDir(directory, password) -> int:
    count = 0
    for dirpath, _dirnames, filenames in os.walk(directory, topdown=False):
        for name in filenames:
            DecryptFile(os.path.join(dirpath, name), password)
            count += 1
    return count
