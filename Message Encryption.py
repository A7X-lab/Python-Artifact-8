# Secret Message Encoder and Decoder Developed By Kirklen Allen

# Function to encode the message
def encrypt_message(message, shift):
    encrypted = ""
    for char in message:
        # Check if character is a letter
        if char.isalpha():
            # Shift within the alphabet and preserve case
            if char.islower():
                encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            # Non-alphabetic characters are added as-is
            encrypted += char
    return encrypted

# Function to decode the message
def decrypt_message(encrypted_message, shift):
    return encrypt_message(encrypted_message, -shift)  # Reverse the shift

# Main Program
print("Welcome to the Secret Message Encoder and Decoder!")
shift = 3  # Shift value for encoding (you can change this)
print(f"Using a shift value of {shift}.")

# Get user input
original_message = input("Enter your message: ")

# Encode the message
encrypted_message = encrypt_message(original_message, shift)
print(f"Encrypted Message: {encrypted_message}")

# Decode the message
decoded_message = decrypt_message(encrypted_message, shift)
print(f"Decoded Message: {decoded_message}")
