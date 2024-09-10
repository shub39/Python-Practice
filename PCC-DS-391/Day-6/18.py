# Check if all items in the tuple are the same.

tuple1 = (45, 45, 45, 45)
def check(t):
  return all(i == t[0] for i in t)
print(check(tuple1))