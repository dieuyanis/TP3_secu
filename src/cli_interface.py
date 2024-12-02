import sys

if __name__ == "__main__":
    command = sys.argv[1]

    if command == "hide":
        input_path = sys.argv[2]
        output_path = sys.argv[3]
        secret = sys.argv[4]
        hide_message(input_path, output_path, secret)
    elif command == "reveal":
        encoded_path = sys.argv[2]
        reveal_message(encoded_path)
    else:
        print("Commandes disponibles :")
        print("  hide <input_image> <output_image> <secret>")
        print("  reveal <encoded_image>")
