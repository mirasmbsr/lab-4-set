s = int(input())
v = set()

for _ in range(s):
    l = input()
    words = l.split()
    v.update(words)
print(len(v))