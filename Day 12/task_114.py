"""
You're building a simple file validator. The system must:
Accept a file header as a string (e.g., "PDF" or "PK" for ZIP files).
Convert this string into a bytes object using the bytes() function.
Compare it to a predefined binary signature (e.g., b'%PDF').
Print whether the file is recognized or unknown.
This teaches how to use the bytes() function for immutable binary data, such as file formats, network communication,
or encoding-sensitive systems.
"""
def validate_file_signature(input_header):
    # Convert input header to bytes
    input_bytes = bytes(input_header, encoding = 'utf-8')

    # Known signatures
    signatures = {
        b'%PDF': 'PDF File',
        b'PK': 'ZIP Archive',
        b'\x89PNG': 'PNG Image'
    }

    # Check for a match
    file_type = signatures.get(input_bytes)
    print(f"Signature: {input_bytes} → Type: {file_type}")

# Run with different inputs
validate_file_signature('%PDF')   # Should detect PDF
validate_file_signature('PK')     # Should detect ZIP
validate_file_signature('TXT')    # Should be unknown
