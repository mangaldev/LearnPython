class hello_training:
    # Constructor default
    # def __init__(self):
    #     print("hello training")
    # Constructor overloading is not allowed
    # def __init__(self, param1, param2):
    #     self.name = param1
    #     self.age = param2
    #     print("hello training {} {}".format(param1, param2))

    #     Constructor overloading is not allowed
    def __init__(self, param1, param2, param3=23, param4=55):
        print("hello training {} {}".format(param1, param2))
        print(f"hello training {param1} {param2}")

    @staticmethod
    def tellMyName():
        print("prints name")

# o1 = hello_training()
o2 = hello_training(param2=27, param4=78, param1="Beacon")
o2.tellMyName()

hello_training.tellMyName()


# print(o2.name)
# print(o2.age)
#
#
# class Person:
#
#     def __init__(self, name="Tom"):
#         self.name = name
#
# # Why do we need this ?
# # Any code/function written outside will execute even with import, if we dont want we should put those in side __main__
# if __name__ == "__main__":
#     p2 = Person("Mark")
#     p1 = Person()
#     p1.show()
#     p2.show()
