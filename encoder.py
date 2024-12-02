import numpy as np
from PIL import Image


class Encoder:
    """
    Classe pour cacher un message dans une image en utilisant la méthode des bits de poids faible (LSB).
    """

    @staticmethod
    def hide_message(input_image_path, output_image_path, secret_message):
        # Charger l'image d'entrée en utilisant PIL (Python Imaging Library).
        # PIL permet de manipuler facilement des images en Python.
        img = Image.open(input_image_path)

        # Convertir l'image en tableau numpy pour faciliter les modifications pixel par pixel.
        # Chaque pixel est représenté sous forme d'une matrice 3D avec ses canaux (R, G, B).
        img_array = np.array(img)

        # Convertir le message secret en une chaîne de bits.
        # Chaque caractère est transformé en un octet binaire (8 bits).
        binary_message = ''.join(format(ord(char), '08b') for char in secret_message)

        # Ajouter un terminateur spécial au message pour indiquer la fin.
        # Ici, le terminateur est un octet NULL (00000000) qui sert de repère pour arrêter l'extraction.
        binary_message += '00000000'

        # Vérifier la capacité de l'image à contenir le message.
        # `height` et `width` représentent les dimensions de l'image, `_` le nombre de canaux (R, G, B).
        height, width, _ = img_array.shape

        # La capacité totale est déterminée par le nombre de bits de poids faible disponibles (1 bit par canal R, G, B).
        max_capacity = height * width * 3
        if len(binary_message) > max_capacity:
            # Lever une exception si le message est trop long.
            raise ValueError("Le message est trop long pour cette image.")

        # Initialisation d'un index pour parcourir les bits du message.
        bit_index = 0

        # Parcourir chaque pixel de l'image.
        for i in range(height):
            for j in range(width):
                for k in range(3):  # Parcourir les trois canaux R, G, B.
                    if bit_index < len(binary_message):
                        # Modifier le bit de poids faible (dernier bit) du canal actuel.
                        # L'opération `(value & ~1)` force le dernier bit à 0,
                        # puis on utilise `|` pour y insérer le bit correspondant du message.
                        img_array[i, j, k] = (img_array[i, j, k] & ~1) | int(binary_message[bit_index])
                        bit_index += 1

        # Créer une nouvelle image à partir du tableau numpy modifié.
        encoded_img = Image.fromarray(img_array)

        # Sauvegarder l'image avec le message caché au chemin spécifié.
        encoded_img.save(output_image_path)

        # Informer l'utilisateur que l'opération a réussi.
        print(f"Message caché avec succès dans {output_image_path}")
