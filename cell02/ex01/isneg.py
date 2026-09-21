num_str = input()
num = int(num_str)

if num < 0:
    print("This number is negative.")
elif num > 0:
    print("This number is positive.")
else:
    print("This number is both positive and negative.")