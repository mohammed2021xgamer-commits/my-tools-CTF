import base64

encoded_text = "U2VjdXJpdHk="
decoded_bytes = base64.b64decode(encoded_text)
decoded_text = decoded_bytes.decode('utf-8')

print("Result:", decoded_text)


import base64

# يطلب منك إدخال النص المشفر
user_input = input("Enter Base64 text: ")

try:
    # فك التشفير وطباعة الناتج الحرفي المباشر
    result = base64.b64decode(user_input).decode('utf-8')
    print("\nResult:", result)
except Exception as e:
    print("\nError: Invalid Base64 string!")

