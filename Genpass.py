import string
from random import random
chars=string.digits+string.ascii_letters+"@#$%"
#chars="koijQh4uW3y1gEM2ftNRrdBT6se5VYw7Ca8U9q0XlIZ#pA$mSOD!cF%/bGPHvJxKLz"
PasswordGen=""
Length=0
Amount=0

while Length<=7:
    Length=int(input("Enter Password's length [8-~]: "))

while Amount==0:
    Amount=int(input("How many? [1 - ~]: "))

for z in range(Amount):
    for x in range(Length):      
        PasswordGen+=chars[int(len(chars)*random())]

    print(PasswordGen, z," # password generated")
    PasswordGen=""
