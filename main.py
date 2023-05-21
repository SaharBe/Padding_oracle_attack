from Cryptodome.Cipher import DES
from Cryptodome.Util.Padding import pad, unpad
import binascii

key = b'poaisfun'  # 8-byte key
iv = b'\x00' * 8  # IV of all zeros


# Step 2
def padding_string(s):
    p_d = s.ljust(16, '\x05')
    padded_bytes = bytes(p_d, 'utf-8')
    return padded_bytes


# Step 3
def pad_plaintext(plaintext, block_size):
    padding_length = block_size - (len(plaintext) % block_size)
    padding = bytes([padding_length] * padding_length)
    return plaintext + padding


def encrypt_padding_string(p_d):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    padded_plaintext = pad_plaintext(p_d, 8)
    ciphertext = cipher.encrypt(padded_plaintext)
    desired_length = 16  # Truncate the ciphertext to the desired length
    truncated_ciphertext = ciphertext[:desired_length]
    cipher_text_hex = binascii.hexlify(truncated_ciphertext).decode('ascii')
    return cipher_text_hex


# Step 4
def decipher_the_ciphertext(cipher_text_hex):
    cipher_text = binascii.unhexlify(cipher_text_hex)  # Ciphertext in hex format
    c = DES.new(key, DES.MODE_CBC, iv)
    decrypted_bytes = c.decrypt(cipher_text)
    plaintext = unpad(decrypted_bytes, DES.block_size).decode('utf-8')
    return plaintext


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Step 2: padding Hello World
    pd = padding_string("Hello World")
    print(pd)

    # Step 3: encrypt the padded string using the DES algorithm in CBC
    ciphertext_hex = encrypt_padding_string(pd)
    print(ciphertext_hex)

    # Step 4: decipher the ciphertext
    decipher = decipher_the_ciphertext(ciphertext_hex)
    print(decipher)
