# Without parameters
def hello_beaconfire():
    print("hello beaconfire")


hello_beaconfire()


def hello_beaconfire_with_params(a, b, c):
    print("hello beaconfire {} {} {}".format(a, b, c))


# hello_beaconfire_with_params(1, 2) # this will an error as we required 3rd argument
hello_beaconfire_with_params(1, 2, "hello")


def hello_beaconfire_with_default_params(a, b, c=None):
    print("hello beaconfire {} {} {}".format(a, b, c))


hello_beaconfire_with_default_params(1, 2) # This will not be ane error as 3rd argument as a default value

