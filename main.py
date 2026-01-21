import json
import sys

# Read input from execution request
input_data = sys.stdin.read()
try:
    data = json.loads(input_data)
except:
    data = {}

name = data.get("name", "Guest")

# Print a message (will appear in logs)
print(f"Hello from Appwrite Function, {name}!")

# Optional output as JSON
output = {"status": "success", "message": f"Hello, {name}"}
print(json.dumps(output))
