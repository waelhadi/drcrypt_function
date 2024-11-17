import base64

def fetch_key_from_github():
    url = "https://raw.githubusercontent.com/waelhadi/art1/main/w1213.txt"
    response = requests.get(url)
    if response.status_code == 200:
        key = int(response.text.strip())
        print("Key fetched successfully:", key)
        return key
    else:
        print(f"Failed to fetch key from GitHub. Status code: {response.status_code}")
        raise Exception("Failed to fetch key from GitHub")

def xor_decrypt(data, key):
    return ''.join(chr(ord(char) ^ key) for char in data)

def decrypt_function(encrypted_parts):
    key = fetch_key_from_github()
    decrypted_parts = []

    # Reverse the encryption layers
    for layer in range(3, 0, -1):
        print(f"Decrypting layer {layer}...")
        decrypted_layer = []

        for part in encrypted_parts:
            decoded_part = base64.b64decode(part).decode()
            decrypted_part = xor_decrypt(decoded_part, key)
            decrypted_layer.append(decrypted_part)

        encrypted_parts = decrypted_layer

    original_code = ''.join(encrypted_parts)
    print("Decryption completed successfully.")
    return original_code
