from PIL import Image
import argparse
import os

# Vérifier et créer les dossiers input et output
os.makedirs("src/input", exist_ok=True)
os.makedirs("src/output", exist_ok=True)

def hide_message(input_image_path, output_image_path, message):
    print(f"Chargement de l'image depuis {input_image_path}")
    image = Image.open(input_image_path)
    encoded_image = image.copy()
    width, height = image.size
    print(f"Dimensions de l'image : {width}x{height}")
    pixels = encoded_image.load()

    # Convertir le message en binaire et ajouter un marqueur de fin
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '11111110'
    print(f"Message binaire : {binary_message}")
    message_index = 0

    for y in range(height):
        for x in range(width):
            pixel = list(pixels[x, y])  # Convert tuple to list
            print(f"Traitement du pixel à la position ({x}, {y}): {pixel}")
            for i in range(3):  # Parcourir les canaux R, G, B
                if message_index < len(binary_message):
                    original_value = pixel[i]
                    pixel[i] = (pixel[i] & ~1) | int(binary_message[message_index])
                    print(f"  Modification du canal {['R', 'G', 'B'][i]} : {original_value} -> {pixel[i]} (bit caché : {binary_message[message_index]})")
                    message_index += 1
            pixels[x, y] = tuple(pixel)
            if message_index >= len(binary_message):
                print(f"Fin du message atteinte au pixel ({x}, {y})")
                print(f"Sauvegarde de l'image encodée dans {output_image_path}")
                encoded_image.save(output_image_path)
                print(f"Message caché avec succès dans {output_image_path}")
                return
    print("L'image est trop petite pour contenir ce message.")

def reveal_message(encoded_image_path):
    """
    Révèle le message caché dans une image encodée.
    :param encoded_image_path: Chemin vers l'image contenant le message encodé.
    """
    print(f"Chargement de l'image encodée depuis {encoded_image_path}...")
    image = Image.open(encoded_image_path)
    pixels = image.load()
    width, height = image.size
    print(f"Dimensions de l'image : {width}x{height}")

    binary_message = ""
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            print(f"Traitement du pixel ({x}, {y}): {pixel}")  # Afficher le pixel actuel
            for i in range(3):  # Parcourir les canaux R, G, B
                # Récupérer le dernier bit de chaque composant de couleur
                binary_message += str(pixel[i] & 1)
                print(f"  Canal {['R', 'G', 'B'][i]}: {pixel[i]} -> bit caché: {pixel[i] & 1}")

    print(f"Message binaire complet : {binary_message[:50]}...")  # Afficher une partie du message binaire pour ne pas trop encombrer le terminal

    # Convertir les bits en caractères
    bytes_message = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    decoded_message = ""
    for byte in bytes_message:
        if byte == "11111110":  # Marqueur de fin
            print("Marqueur de fin trouvé. Fin du message.")
            break
        decoded_message += chr(int(byte, 2))

    if decoded_message:
        print(f"Message révélé : {decoded_message}")
    else:
        print("Aucun message n'a été trouvé.")

    return decoded_message

# Exemple d'utilisation
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cacher ou révéler un message dans une image.")
    parser.add_argument("mode", choices=["hide", "reveal"], help="Mode : 'hide' pour cacher, 'reveal' pour révéler.")
    parser.add_argument("input", help="Chemin de l'image d'entrée.")
    parser.add_argument("output", nargs="?", help="Chemin de l'image de sortie (pour 'hide').")
    parser.add_argument("message", nargs="?", help="Message à cacher (pour 'hide').")

    args = parser.parse_args()

    if args.mode == "hide":
        if not args.output or not args.message:
            print("Pour le mode 'hide', vous devez fournir un chemin de sortie et un message.")
        else:
            hide_message(args.input, args.output, args.message)
    elif args.mode == "reveal":
        reveal_message(args.input)
