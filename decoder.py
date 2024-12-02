import numpy as np
from PIL import Image


class Decoder:
    """
    Classe pour extraire un message caché dans une image en utilisant la méthode des bits de poids faible (LSB).
    """

    @staticmethod
    def reveal_message(encoded_image_path):
        # Charger l'image avec le message caché en mémoire.
        img = Image.open(encoded_image_path)

        # Convertir l'image en tableau numpy pour faciliter la lecture des pixels.
        img_array = np.array(img)

        # Initialiser une chaîne vide pour stocker les bits extraits.
        binary_message = ""

        # Parcourir chaque pixel de l'image.
        for row in img_array:
            for pixel in row:
                for color in pixel:
                    # Extraire le bit de poids faible (dernier bit) de chaque canal (R, G, B).
                    # Le bit de poids faible est obtenu avec l'opération `& 1` (ET logique).
                    binary_message += str(color & 1)

        # Initialiser une chaîne pour stocker le message final.
        message = ""

        # Regrouper les bits en octets de 8 bits, puis les convertir en caractères.
        for i in range(0, len(binary_message), 8):
            # Chaque groupe de 8 bits est traité comme un caractère.
            byte = binary_message[i:i + 8]

            # Convertir l'octet binaire en entier (base 2), puis en caractère ASCII.
            char = chr(int(byte, 2))

            # Arrêter la lecture si le terminateur est rencontré (caractère NULL).
            if char == '\x00':
                break

            # Ajouter le caractère au message final.
            message += char

        # Afficher le message extrait pour l'utilisateur.
        print(f"Message extrait : {message}")
        return message
