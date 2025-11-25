import string
import os

ALPH = string.ascii_uppercase


def parse_config(filename):
    r1 = r2 = r3 = refl = None
    with open(filename, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.lower().startswith("rotor1:"):
                r1 = line.split(":", 1)[1].strip().upper()
            elif line.lower().startswith("rotor2:"):
                r2 = line.split(":", 1)[1].strip().upper()
            elif line.lower().startswith("rotor3:"):
                r3 = line.split(":", 1)[1].strip().upper()
            elif line.lower().startswith("reflector:"):
                refl = line.split(":", 1)[1].strip().upper()
    return list(r1), list(r2), list(r3), list(refl)


def encrypt_forward(idx, rotor, pos):
    shifted = (idx + pos) % 26
    return (ALPH.index(rotor[shifted]) - pos) % 26


def encrypt_reverse(idx, rotor, pos):
    shifted = (idx + pos) % 26
    letter = ALPH[shifted]
    i = rotor.index(letter)
    return (i - pos) % 26


def advance(positions):
    positions[2] = (positions[2] + 1) % 26


def encrypt_char(ch, rotors, reflector, positions):
    if ch not in ALPH:
        return ch

    advance(positions)
    r1, r2, r3 = rotors

    idx = ALPH.index(ch)

    idx = encrypt_forward(idx, r1, positions[0])
    idx = encrypt_forward(idx, r2, positions[1])
    idx = encrypt_forward(idx, r3, positions[2])

    idx = ALPH.index(reflector[idx])

    idx = encrypt_reverse(idx, r3, positions[2])
    idx = encrypt_reverse(idx, r2, positions[1])
    idx = encrypt_reverse(idx, r1, positions[0])

    return ALPH[idx]


def main():
    cfg = input("Insert config(filename): ").strip()
    if not os.path.exists(cfg):
        print("Config not found.")
        return

    r1, r2, r3, reflector = parse_config(cfg)

    plugs = input("Insert plugs (y/n)?: ").strip().lower()
    print(
        "No extra plugs inserted."
        if plugs != "y"
        else "Plugboard skipped (not implemented)."
    )

    print("Enigma initialized.")
    rotors = (r1, r2, r3)

    while True:
        row = input("\nInsert row (empty stops): ")
        if row == "":
            print("\nEnigma closing.")
            break

        positions = [0, 0, 0]
        out = []

        for c in row:
            up = c.upper()
            if up in ALPH:
                res = encrypt_char(up, rotors, reflector, positions)
                print(f'Character "{c}" illuminated as "{res}"')
                out.append(res)
            else:
                print(f'Character "{c}" illuminated as "{c}"')
                out.append(c)

        print(f'Converted row - "{''.join(out)}".')


if __name__ == "__main__":
    main()
