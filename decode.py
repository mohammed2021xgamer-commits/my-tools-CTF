import base64

user_input = input("Enter Base64 text: ")

try:
    result = base64.b64decode(user_input).decode('utf-8')
    print("\nResult:", result)
except Exception as e:
    print("\nError: Invalid Base64 string!")

