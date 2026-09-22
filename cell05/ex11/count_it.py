#!/usr/bin/env python3
import sys

def main():
    params = sys.argv[1:]

    if not params:
        print("none")
        return

    print(f"parameters: {len(params)}")

    for param in params:
        print(f"{param}: {len(param)}")

if __name__ == "__main__":
    main()