def caesar_brute_force(ciphertext):
    print("Brute Force Results:")
    for key in range(1, 26):
        decrypted = ""
        for char in ciphertext:
            if char.isalpha():
                shift = 65 if char.isupper() else 97
                decrypted += chr((ord(char) - shift - key) % 26 + shift)
            else:
                decrypted += char
        print(f"Key {key}: {decrypted}")

# Example usage:
cipher = "Wklv lv d vhfuhw phvvdjh"  # "This is a secret message" with shift = 3
caesar_brute_force(cipher)
