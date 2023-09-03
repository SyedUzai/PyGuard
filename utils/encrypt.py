# Import the required modules
from crypto.Cipher import AES
from crypto.Util.Padding import pad, unpad
from crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

# Define the encryption function
def encrypt_AES_CBC_256(key, password):
    key_bytes = key.encode('utf-8')
    message_bytes = password.encode('utf-8')
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    padded_message = pad(message_bytes, AES.block_size)
    ciphertext_bytes = cipher.encrypt(padded_message)
    ciphertext = b64encode(iv + ciphertext_bytes).decode('utf-8')
    return ciphertext

# Define the decryption function
def decrypt_AES_CBC_256(key, ciphertext):
    key_bytes = key.encode('utf-8')
    ciphertext_bytes = b64decode(ciphertext)
    iv = ciphertext_bytes[:AES.block_size]
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    ciphertext_bytes = ciphertext_bytes[AES.block_size:]
    decrypted_bytes = cipher.decrypt(ciphertext_bytes)
    plaintext_bytes = unpad(decrypted_bytes, AES.block_size)
    plaintext = plaintext_bytes.decode('utf-8')
    return plaintext
