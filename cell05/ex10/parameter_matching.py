#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) - 1 != 1:
        print("none")
        return

    expected_param = sys.argv[1]
    
    user_input = input("What was the parameter? ")

    if user_input == expected_param:
        print("Good job!")
    else:
        print("Nope, sorry...")

if __name__ == "__main__":
    main()