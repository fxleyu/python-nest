# 8.1
L = range(1, 101)

print L[:10]
print L[2::3]
print L[4:50:5]

# 8.2
L = range(1, 101)
print L[-10:]
print L[-46::5]

# 8.3
def firstCharUpper(s):
    return s[0].upper() + s[1:]

print firstCharUpper('hello')
print firstCharUpper('sunday')
print firstCharUpper('september')