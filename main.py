import os

JOKE = (
    "I gave my AI agent a rubber duck for debugging. "
    "Three hours later the duck had a GitHub account and two approved pull requests."
)


def main():
    out = os.environ.get("OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(out)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
