for i in range(11, 0, -2):
  print()
  print(" " * (5-i//2), end="")
  for j in range(65, 65 + i):
    print(chr(j), end="")