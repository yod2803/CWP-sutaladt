#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) - 1 != 2:
        print("none")
        return

    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
    except ValueError:
        print("none")
        return

    if start <= end:
        result = list(range(start, end + 1))
    else:
        result = list(range(start, end - 1, -1))

    print(result)

if __name__ == "__main__":
    main()