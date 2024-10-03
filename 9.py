import random

import string

a = string.ascii_letters + string.digits + string.punctuation

p = ''.join(random.choice(a) for _ in range(8))

print(p)
