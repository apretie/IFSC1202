f1 = 0
f2 = 1
f3 = 1
i = 1
seq = int(input("Enter Fibonnaci Sequence Number: "))
while i < seq:
  i += 1
  f3 = f1 + f2
  # multiple assignment below - same as
  # f1 = f2
  # f2 = f3
  f1, f2 = f2, f3
print("Fibonacci Number:", f3)