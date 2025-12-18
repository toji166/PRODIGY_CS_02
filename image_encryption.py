from PIL import Image
import numpy as np

# ENCRYPT IMAGE
def encrypt_image(input_path, output_path, key):
    # Load image as RGB (ignore PNG palette warnings)
    image = Image.open(input_path).convert("RGB")
    pixels = np.array(image, dtype=np.uint8)

    # Convert to uint16 to avoid overflow
    pix16 = pixels.astype(np.uint16)

    # 1) Shift pixel values
    pix16 = (pix16 + key) % 256

    # 2) XOR for extra encryption strength
    pix16 = pix16 ^ key

    # Convert back to uint8
    encrypted_pixels = pix16.astype(np.uint8)

    encrypted_image = Image.fromarray(encrypted_pixels)
    encrypted_image.save(output_path)
    print("Encrypted image saved:", output_path)

# DECRYPT IMAGE
def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path).convert("RGB")
    pixels = np.array(image, dtype=np.uint8)

    pix16 = pixels.astype(np.uint16)

    # 1) Reverse XOR
    pix16 = pix16 ^ key

    # 2) Reverse shift
    pix16 = (pix16 - key) % 256

    decrypted_pixels = pix16.astype(np.uint8)

    decrypted_image = Image.fromarray(decrypted_pixels)
    decrypted_image.save(output_path)
    print("Decrypted image saved:", output_path)

key = 50

encrypt_image("input_image.png", "encrypted_image.png", key)
decrypt_image("encrypted_image.png", "decrypted_image.png", key)
