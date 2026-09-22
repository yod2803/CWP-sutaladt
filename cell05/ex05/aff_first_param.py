#!/usr/bin/env python3
import sys

def main():
    # sys.argv[0] is the script name. If len is > 1, at least one parameter was passed.
    if len(sys.argv) > 1:
        print(sys.argv[1])
    else:
        print("none")

if __name__ == "__main__":
    main()