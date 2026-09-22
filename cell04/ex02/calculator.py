def main():
    first = int(input("Give me the first number: "))
    second = int(input("Give me the second number: "))
    
    print("Thank you!")
    print(f"{first} + {second} = {first + second}")
    print(f"{first} - {second} = {first - second}")
    print(f"{first} / {second} = {first // second if second != 0 else 'Error: Division by zero'}")
    print(f"{first} * {second} = {first * second}")

if __name__ == "__main__":
    main()