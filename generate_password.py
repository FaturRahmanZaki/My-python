s

import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"

all = lower + upper + number
length = "16"
password = "".join(random.sample(all,length))

print(password)