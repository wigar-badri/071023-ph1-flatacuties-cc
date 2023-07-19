#!/usr/bin/env python3
import os

if __name__ == "__main__":
    name = input("Enter your name: ").lower().strip().replace(" ", "-")
    print(" ")

    if name and len(name) > 2:
        try:
            os.system("git add . && git commit --allow-empty -m \"Final commit\"")
            os.system(f"git bundle create ../{name}-ph1-flatacuties.bundle HEAD #{name}")
            print("\nBundling complete, submit on Canvas")
        except Exception as e:
            print("There was an error:")
            print(e)
    else:
        print("Invalid name (must be at least 3 characters), please try again")
