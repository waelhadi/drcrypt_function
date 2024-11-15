import base64, requests

def fetch_key():
    # المفتاح المشفر
    encrypted_key = "MTIzNDU2"  # المفتاح مشفر هنا باستخدام base64
    # فك تشفير المفتاح عند الحاجة
    key = int(base64.b64decode(encrypted_key).decode())
    return key

def xor_decrypt(data, key):
    return ''.join(chr(ord(char) ^ key) for char in data)

def decrypt_function(encrypted_parts):
    parts = encrypted_parts
    key = fetch_key()  # جلب المفتاح وفك تشفيره عند الحاجة

    # فك التشفير عبر الطبقات
    for layer in range(3, 0, -1):  # بدءاً من الطبقة الأخيرة إلى الطبقة الأولى
        decrypted_parts_layer = []

        for part in parts:
            # فك الترميز مع معالجة الأحرف غير المدعومة
            decoded_part = base64.b64decode(part).decode('utf-8', errors='replace')
            decrypted_part = xor_decrypt(decoded_part, key)
            decrypted_parts_layer.append(decrypted_part)

        parts = decrypted_parts_layer

    return ''.join(parts)  # إرجاع الكود الأصلي كنص واحد
