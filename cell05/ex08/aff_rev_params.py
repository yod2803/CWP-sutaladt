#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) - 1 < 2:
        print("none")
    else:
        for param in reversed(sys.argv[1:]):
            print(param)

if __name__ == "__main__":
    main()