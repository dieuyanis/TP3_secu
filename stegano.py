import argparse
from stegano.encoder import Encoder
from stegano.decoder import Decoder
from stegano.utils import Utils

def main():
    parser = argparse.ArgumentParser(description="Application de stéganographie en CLI.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Commande pour cacher un message
    hide_parser = subparsers.add_parser("hide", help="Cacher un message dans une image.")
    hide_parser.add_argument("input_image", type=str, help="Chemin de l'image d'entrée.")
    hide_parser.add_argument("output_image", type=str, help="Chemin de l'image de sortie.")
    hide_parser.add_argument("message", type=str, help="Message secret à cacher.")

    # Commande pour révéler un message
    reveal_parser = subparsers.add_parser("reveal", help="Révéler un message caché dans une image.")
    reveal_parser.add_argument("encoded_image", type=str, help="Chemin de l'image encodée.")

    args = parser.parse_args()

    if args.command == "hide":
        Utils.validate_image_format(args.input_image)
        Utils.validate_image_format(args.output_image)
        Encoder.hide_message(args.input_image, args.output_image, args.message)
    elif args.command == "reveal":
        Utils.validate_image_format(args.encoded_image)
        Decoder.reveal_message(args.encoded_image)

if __name__ == "__main__":
    main()
