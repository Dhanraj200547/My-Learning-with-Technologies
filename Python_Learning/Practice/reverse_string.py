s = "Hello"
b = ""
a = "".join(reversed(s))
print(a)


for i in range(len(s)-1,-1,-1):
    b += s[i]

print(b)

#slicing
print(s[::-1])