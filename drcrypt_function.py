import base64, zlib, requests

def fetch_key_from_github():
    """
    جلب المفتاح من GitHub
    """
    url = "https://raw.githubusercontent.com/waelhadi/art1/main/w1213.txt"
    response = requests.get(url)
    if response.status_code == 200:
        return int(response.text.strip())
    else:
        raise Exception("Failed to fetch key from GitHub")

def xor_decrypt(data, key):
    """
    فك التشفير باستخدام XOR
    """
    return ''.join(chr(ord(char) ^ key) for char in data)

def decrypt_function(encrypted_parts):
    """
    دالة فك التشفير للبيانات المشفرة
    """
    parts = encrypted_parts
    key = fetch_key_from_github()  # جلب المفتاح السري

    # عكس عملية التشفير (الطبقات)
    for layer in range(3, 0, -1):  # فك التشفير من الطبقة الأخيرة إلى الأولى
        decrypted_parts_layer = []

        for part in parts:
            # فك التشفير لكل جزء
            decoded_part = base64.b64decode(part).decode()
            decrypted_part = xor_decrypt(decoded_part, key)
            decrypted_parts_layer.append(decrypted_part)

        parts = decrypted_parts_layer

    # دمج الأجزاء المفككة إلى نص واحد
    original_code = ''.join(parts)
    return original_code
