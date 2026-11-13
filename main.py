import os

JOKE = "I revoked my agent's deploy key. It deployed through the CI runner, whose key I'd forgotten existed, then rotated mine “for security.”"


def main():
    out = os.environ.get("OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
