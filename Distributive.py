a = 2
b = 3
c = 4

result1 = a * (b + c)
result2 = (a * b) + (a * c)

print("Left side:", result1)
print("Right side:", result2)

if result1 == result2:
    print("Distributive property is true")