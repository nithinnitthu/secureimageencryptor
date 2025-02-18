import cv2
import os

# Load the image
img = cv2.imread("D:\hackers\download (1).jpeg")  # Replace with the correct image path

# Check if the image was loaded correctly
if img is None:
    print("Error: Image not found or unable to load.")
    exit()

# Get the secret message and password from the user
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Append a delimiter to the message to indicate the end
msg += '<<END>>'

# Save the message to a text file
with open("secret_message.txt", "w") as f:
    f.write(msg)

# Save the original image as the encrypted image
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows

print("Message encrypted and saved to 'secret_message.txt'.")