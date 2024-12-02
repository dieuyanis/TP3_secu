def reveal_message(encoded_image_path):
    image = Image.open(encoded_image_path)
    pixels = image.load()
    width, height = image.size

    binary_message = ''
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            for i in range(3):  # Iterate through R, G, B channels
                binary_message += str(pixel[i] & 1)

    # Convert binary message to string
    bytes_message = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    decoded_message = ''.join([chr(int(byte, 2)) for byte in bytes_message])

    # Stop decoding at delimiter
    end_delimiter = decoded_message.find('\xFE')  # '\xFE' corresponds to 11111110
    if end_delimiter != -1:
        decoded_message = decoded_message[:end_delimiter]

    print(f"Message révélé : {decoded_message}")
