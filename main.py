def main(context):
    # Access input payload like this:
    data = context.payload  # this is a dictionary
    name = data.get("name", "Guest")

    print(f"Hello from Appwrite Function, {name}!")

    # Return a dictionary as output
    return {"status": "success", "message": f"Hello, {name}"}
