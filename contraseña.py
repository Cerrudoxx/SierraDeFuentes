import base64

def generate_password():
    encoded_password = b'UDBsNGMxMEQzQzBuZ3Izcw=='
    decoded_password = base64.b64decode(encoded_password).decode('utf-8')
    return decoded_password

password = generate_password()
print(password)