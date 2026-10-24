import secrets
import string

length = 16
chars = string.ascii_letters + string.digits + string.punctuation

# secrets.choice делает генерацию криптографически стойкой
password = ''.join(secrets.choice(chars) for _ in range(length))

print(f"Надежный пароль: {password}")
