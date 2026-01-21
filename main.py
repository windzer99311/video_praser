import json
import sys

# Appwrite will call this
def main(args):
    # args is a dictionary with input data
    name = args.get("name", "Guest")

    # Your function logic
    print(f"Hello from Appwrite Function, {name}!")

    # Optional output
    output = {"status": "success", "message": f"Hello, {name}"}
    return output
