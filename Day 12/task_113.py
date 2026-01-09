"""
You're tasked with simulating secure data processing where:
A plain-text message is converted into bytes using bytearray().
You then modify the content (simulate encryption by shifting each byte by +1).
Print the original and "encrypted" message.
This task demonstrates how bytearray() allows mutable byte-level manipulation, often needed in data processing,
low-level I/O, or network communication.
"""
def simulate_encryption(message):
    # Convert string to bytearray
    byte_data = bytearray(message, "utf-8")

    # Encrypt: Shift each byte by +1
    for i in range(len(byte_data)):
        byte_data[i] += 1

    print("Encrypted Byte Values:", list(byte_data))

    # Convert back to string (for demonstration)
    encrypted_message = byte_data.decode('utf-8', errors='replace')
    return encrypted_message

# Run the function
plain_text = "Secure123!"
encrypted = simulate_encryption(plain_text)
print("Encrypted Message:", encrypted)
