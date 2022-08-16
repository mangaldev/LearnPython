# a  = "Beacon"
#
# print(a[0:2])
#
# print(a[1:4])
#
# a =  "asdfsfdsfsdfds" \
#      "sdfsdfsfdsdfsdf" \
#      "sdfsdfsdfs" \
#
# a = """
# sdfsdfsfs \b \b
# fsdf
# sdf
# sdf
# sdf
# s
# """


a = 10
b = str(a)

print(type(b))

a = "hello"
b = "world"
print(a + " " + b)

a = "hello"
print(a[1])


y = "      Hello   World ... \n\n"
print(y.strip())


a = "Hello World"
print(a.lower())
print(a.upper())

print(a.startswith("hello"))
print(a.startswith("Hello"))
print(a.endswith("ld"))

print(a.find("World"))

print(a.replace("World","Kitty"))

print(len(a))

index = a.find("World")
if index > 0:
    print(True)

print( "World" in a)



