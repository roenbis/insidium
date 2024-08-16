import random
import string

def shuffle(string):
    temp_list = list(string)
    random.shuffle(temp_list)
    return ''.join(temp_list)

uppercase_letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
digits = ''.join(random.choice(string.digits) for _ in range(2))
special_char = random.choice('@#$')
lowercase_letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(16))

password = uppercase_letters + digits + special_char + lowercase_letters

password = shuffle(password)

print(password)
