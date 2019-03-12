s = {10, 20, 30, 40}
print(s)
s.add(50)
print(s)
s.remove(30)
print(s)
fs = frozenset(s)
print(fs)
print(type(fs))