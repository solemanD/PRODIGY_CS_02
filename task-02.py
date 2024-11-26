from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    """
    Encrypts the image using XOR operation and channel swapping.
    """
    try:
        # Open the image and convert it to a NumPy array
        img = Image.open(input_path)
        img_array = np.array(img)

        # XOR operation with the key
        encrypted_array = img_array ^ key

        # Swap the color channels for added randomness (optional)
        if len(encrypted_array.shape) == 3:  # RGB image
            encrypted_array = encrypted_array[:, :, ::-1]

        # Convert back to an image and save
        encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
        encrypted_img.save(output_path)
        print(f"Image encrypted successfully and saved to {output_path}")
    except Exception as e:
        print(f"Error during encryption: {e}")

def decrypt_image(input_path, output_path, key):
    """
    Decrypts the image by reversing the XOR operation and channel swapping.
    """
    try:
        # Open the encrypted image and convert it to a NumPy array
        img = Image.open(input_path)
        img_array = np.array(img)

        # Reverse channel swapping
        if len(img_array.shape) == 3:  # RGB image
            img_array = img_array[:, :, ::-1]

        # Reverse the XOR operation
        decrypted_array = img_array ^ key

        # Convert back to an image and save
        decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
        decrypted_img.save(output_path)
        print(f"Image decrypted successfully and saved to {output_path}")
    except Exception as e:
        print(f"Error during decryption: {e}")

def main():
    """
    Main program to interact with the user.
    """
    print("Image Encryption Tool")
    print("=====================")
    
    while True:
        print("\nMenu:")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            input_path = input("Enter the path to the image to encrypt: ")
            output_path = input("Enter the path to save the encrypted image: ")
            key = int(input("Enter an encryption key (integer): "))
            encrypt_image(input_path, output_path, key)
        elif choice == "2":
            input_path = input("Enter the path to the encrypted image: ")
            output_path = input("Enter the path to save the decrypted image: ")
            key = int(input("Enter the decryption key (integer): "))
            decrypt_image(input_path, output_path, key)
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
