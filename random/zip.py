a = ("A", "B", "C", "D")
b = ("a", "b", "c")
c = ("1","2","3")

x = zip(a, b, c)

print(type(x))
print(x)
for item in x:
    print(type(item))
    print(item)

# ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
languages = ['Java', 'Python', 'JavaScript']
versions = [14, 3, 6]

result = zip(languages, versions)
print(result)
listedZip = list(result)
print(listedZip)
print(listedZip[1][1])

# Output: [('Java', 14), ('Python', 3), ('JavaScript', 6)]
# ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

