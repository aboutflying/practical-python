# bounce.py
#
# Exercise 1.5

height = 100
bounce = 1

while bounce <= 10:
    height *= (3/5)
    print(bounce, round(height, ndigits=4))
    bounce += 1