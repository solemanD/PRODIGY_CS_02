# PRODIGY_CS_02

## Task Description

> - Develop a simple image encryption tool using pixel manipulation. You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. Allow users to encrypt and decrypt images.

-> Here's a Python program that implements a simple image encryption tool using pixel manipulation. It allows users to encrypt and decrypt images by swapping pixel values or applying a basic mathematical operation on each pixel.

### Program Features

1. Image Encryption:

> - Performs a reversible mathematical operation (e.g., XOR with a key) on each pixel value.
>   Optionally swaps color channels to add more randomness.

2. Image Decryption:

> - Applies the inverse of the encryption process to restore the original image.

3. User Interaction:

   > - User specifies the image file, encryption/decryption key, and the desired operation (encrypt or decrypt).

4. Python Libraries:
   > - Pillow (PIL): For loading, manipulating, and saving images.
   > - Built-in libraries for handling file operations.

## Implementation

> with python

## How It Works

1. Encryption:

> - Each pixel value in the image is XORed with the provided key.
> - If the image is in RGB format, the color channels (R, G, B) are optionally swapped for added randomness.
>
> 2. Decryption:

> - Swaps the color channels back to their original order.
> - Reapplies the XOR operation with the same key to restore the original pixel values.

## Usage Instructions

1. Install the Pillow library if not already installed:
   > - pip install pillow
2. Run the script:
   > - python task-02.py
3. Follow the interactive menu:
   > - Enter the file path to your input image.
   > - Provide an output path where the encrypted/decrypted image will be saved.
   > - Specify an integer key for encryption or decryption (same key is used for both).
