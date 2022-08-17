import sys

while True:
    try:
        x = int(input("x = "))
        if x <= 0:
            raise ValueError
    except ValueError:
        print("Please enter a valid, positive number")
        pass
    else:
        print("\U0001f36a"*x)
        sys.exit()
