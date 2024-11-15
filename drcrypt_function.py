import base64, requests

def fetch_key():

	encrypted_key = "MTIzNDU2"  
    key = int(base64.b64decode(encrypted_key).decode())
    return key

def xor_decrypt(data, key):
    return ''.join(chr(ord(char) ^ key) for char in data)

def decrypt_function(encrypted_parts):
    parts = encrypted_parts
    key = fetch_key()   

    for layer in range(3, 0, -1):   
        decrypted_parts_layer = []

        for part in parts:
            decoded_part = base64.b64decode(part).decode('utf-8')  
            decrypted_part = xor_decrypt(decoded_part, key)
            decrypted_parts_layer.append(decrypted_part)

        parts = decrypted_parts_layer

    return ''.join(parts)   
