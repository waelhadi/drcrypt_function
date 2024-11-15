import requests, zlib, base64

def fetch_decryption_function():
    url = "https://raw.githubusercontent.com/username/repo/main/drcrypt_function.py"  # رابط الملف على GitHub
    response = requests.get(url)
    if response.status_code == 200:
        exec(response.text, globals())  # تحميل الدالة إلى النطاق العام
        print("Decryption function loaded successfully.")
    else:
        raise Exception("Failed to fetch decryption function from GitHub")

# استدعاء دالة جلب دالة فك التشفير
fetch_decryption_function()

# الآن يمكنك استخدام decrypt_function بعد تحميلها
try:
    # على سبيل المثال، قم بتمرير البيانات المشفرة إلى decrypt_function
    with open("encrypted_data.txt", "rb") as f:
        encrypted_parts = eval(zlib.decompress(f.read()).decode())

    original_code = decrypt_function(encrypted_parts)
    print("Decrypted Code:")
    print(original_code)
except Exception as e:
    print(f"Error during decryption: {e}")
