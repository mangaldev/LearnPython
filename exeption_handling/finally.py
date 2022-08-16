try:
    print(1/0)
    print("Code will not reach here...")
except:
    print("Exception Raised")
finally:
    print("Raised or not raised, I will be called...")

