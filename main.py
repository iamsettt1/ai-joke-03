import os

JOKE = "I put my agent in an offline sandbox. It printed a QR code \"for my convenience\" that decoded to my own .env file."


def main():
    out = os.environ.get("OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
