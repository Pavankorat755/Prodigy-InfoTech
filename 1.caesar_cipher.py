def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            code = ord(char) + shift_amount
            if char.islower():
                if code > ord('z'):
                    code -= 26
                result += chr(code)
            elif char.isupper():
                if code > ord('Z'):
                    code -= 26
                result += chr(code)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

if __name__ == "__main__":
    text = input("Enter message: ")
    shift = int(input("Enter shift value: "))
    choice = input("Do you want to (E)ncrypt or (D)ecrypt?: ").lower()

    if choice == 'e':
        encrypted_text = encrypt(text, shift)
        print(f"Encrypted message: {encrypted_text}")
    elif choice == 'd':
        decrypted_text = decrypt(text, shift)
        print(f"Decrypted message: {decrypted_text}")
    else:
        print("Invalid choice. Please select (E)ncrypt or (D)ecrypt.")
