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
        print("Amount of cookies in cookie jar")
        print("\U0001f36a"*x)
        y = int(x/2)
        print("Amount you can eat")
        print("\U0001f36a"*y)
        sys.exit()
