a, b = 0, 1
count = 0
total = 0
while b < 100:
    print(b)
    total += b
    count += 1
    a, b = b, a + b
average = total / count
print(f"\nAverage: {average:.2f}")
