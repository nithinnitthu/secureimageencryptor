# Get the password for decryption
password = input("Enter passcode for Decryption: ")

# Read the message from the text file
try:
    with open("secret_message.txt", "r") as f:
        message = f.read()
except FileNotFoundError:
    print("Error: Secret message file not found.")
    exit()

# Check the password
if password == input("Enter the correct passcode: "):
    # Remove the delimiter and print the message
    if message.endswith('<<END>>'):
        message = message[:-8]  # Remove the delimiter
    print("Decrypted message:", message)
else:
    print("YOU ARE NOT authorized")