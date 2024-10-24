from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    pixels = np.array(image)
    
    np.random.seed(key)
    encrypted_pixels = pixels.copy()
    height, width, _ = pixels.shape
    for i in range(height):
        for j in range(width):
            encrypted_pixels[i, j] = (pixels[i, j] + np.random.randint(0, 256, 3)) % 256
            
    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'), 'RGB')
    encrypted_image.save("encrypted_image.png")

def decrypt_image(image_path, key):
    image = Image.open(image_path)
    pixels = np.array(image)
    
    np.random.seed(key)
    decrypted_pixels = pixels.copy()
    height, width, _ = pixels.shape
    for i in range(height):
        for j in range(width):
            decrypted_pixels[i, j] = (pixels[i, j] - np.random.randint(0, 256, 3)) % 256
            
    decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'), 'RGB')
    decrypted_image.save("decrypted_image.png")

if __name__ == "__main__":
    choice = input("Do you want to (E)ncrypt or (D)ecrypt an image?: ").lower()
    image_path = input("Enter the path to the image: ")
    key = int(input("Enter a key (integer) for encryption/decryption: "))

    if choice == 'e':
        encrypt_image(image_path, key)
        print("Image encrypted and saved as 'encrypted_image.png'.")
    elif choice == 'd':
        decrypt_image(image_path, key)
        print("Image decrypted and saved as 'decrypted_image.png'.")
    else:
        print("Invalid choice. Please select (E)ncrypt or (D)ecrypt.")
