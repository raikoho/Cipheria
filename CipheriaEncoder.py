import random


# ANSI-коди для кольорів
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# ASCII Art Logo
def print_intro():
    print(f"""
{Colors.OKGREEN}
****** * ***** ***** * * **** * * ********* **** *** 
                                                     
 ╟ ƒ  ¥ ►   ╜   ¿ ¥ ♣  ►   ¥   ≈  ■ ¥   ≈  ¥    τ ╢  
   ■     ▓ ╜  Θ  π     ¿ ß ╜ ╜ ┴ ►τ ª ßτ ≡   τ Θ     
     ½ Θ     ≈ ¿    ß ▓   τ   ßτ π  τ   ½  ▓   α  ╢  
 ╟ Æ¢  ≡  ¥ ┴  ♣ ¼  α  ¥   ¿ ▓ τ  ªτ    ¥  ► ƒ π     
   d  ½♣α    ≡ƒ   ▓  τ ¿  Θ   k   ½►  ▓   ┴   Θ  ≈   
   Γ    ► ≡   ≡  ¿  ▓  ♣  xτ► qwe ╦ π Σ  ►    ♣  π   
 ╟ Æ ♣   ▓     ►  Γ  τ ♣    Θ  b  h  y    ■ ¥  π     
   ¿   ▓  ¥  ╦ ┴ Γ ¥ ╗ « ┴  ■ ¿  ┴ Θ   ╗  ♣   ╗   ╢  
                                                     
****** ******* ************ ******** ********* ******
{Colors.ENDC}
{Colors.OKCYAN}Cipheria - created by Bohdan Misonh{Colors.ENDC}
{Colors.OKCYAN}Version 1.0{Colors.ENDC}
{Colors.HEADER}---------------------------------{Colors.ENDC}
""")

# Базові шифри

def caesar_cipher(text, shift):
    """Encrypts text using Caesar cipher with a given shift."""
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result


def vigenere_cipher(text, key):
    """Encrypts text using Vigenère cipher with a given key."""
    result = []
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    text_as_int = [ord(i) for i in text]
    for i in range(len(text_as_int)):
        if text[i].isalpha():
            value = (text_as_int[i] + key_as_int[i % key_length]) % 26
            if text[i].isupper():
                result.append(chr(value + 65))
            else:
                result.append(chr(value + 97))
        else:
            result.append(text[i])
    return ''.join(result)


def atbash_cipher(text):
    """Encrypts text using Atbash cipher."""
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr(90 - (ord(char) - 65))
            else:
                result += chr(122 - (ord(char) - 97))
        else:
            result += char
    return result


def scytale_cipher(text, shift):
    """Encrypts text using Scytale cipher with a given shift."""
    result = [''] * shift
    for i, char in enumerate(text):
        result[i % shift] += char
    return ''.join(result)


def vernam_cipher(text, key):
    """Encrypts text using Vernam cipher with a given key."""
    encrypted = "".join(chr(ord(char) ^ ord(key[i])) for i, char in enumerate(text))
    return encrypted


def rail_fence_cipher(text, num_rails):
    """Encrypts text using Rail Fence cipher with a given number of rails."""
    rails = [''] * num_rails
    rail = 0
    direction = 1
    for char in text:
        rails[rail] += char
        rail += direction
        if rail == 0 or rail == num_rails - 1:
            direction *= -1
    return ''.join(rails)


def affine_cipher(text, a, b):
    """Encrypts text using Affine cipher with given 'a' and 'b' values."""

    def modular_inverse(a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

    m = 26  # Number of letters in the English alphabet
    encrypted = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            encrypted += chr(((a * (ord(char) - offset) + b) % m) + offset)
        else:
            encrypted += char
    return encrypted


def custom_cipher(text, key_file):
    """Encrypts text using a custom cipher defined in the key file."""
    with open(key_file, 'r', encoding='utf-8') as file:
        key_map = dict(line.strip().split('=') for line in file if '=' in line)

    result = ""
    for char in text:
        result += key_map.get(char, char)  # Replace character if in key, else leave unchanged
    return result


# Функція для зчитування тексту з файлу
def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


# Функція для запису зашифрованого тексту у файл
def write_text_to_file(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)


# Функція для шифрування тексту
def encrypt_text(text, cipher_func, *args):
    return cipher_func(text, *args)


# Словник шифрів
ciphers = {
    'caesar': (caesar_cipher,
               "Caesar Cipher: Each letter in the plaintext is shifted a certain number of places down or up the alphabet. Example: 'A' with a shift of 3 becomes 'D'."),
    'vigenere': (vigenere_cipher,
                 "Vigenère Cipher: Uses a keyword to shift letters in the plaintext. Example: 'HELLO' with key 'KEY' becomes 'RIJVS'."),
    'atbash': (
    atbash_cipher, "Atbash Cipher: Each letter of the alphabet is mapped to its reverse. Example: 'A' becomes 'Z'."),
    'scytale': (scytale_cipher,
                "Scytale Cipher: Text is written in a zigzag pattern over multiple 'rails' and read off vertically. Example: 'HELLO WORLD' with 3 rails."),
    'vernam': (vernam_cipher,
               "Vernam Cipher: Uses a random key to XOR with the plaintext. Each letter is encrypted with a corresponding letter in the key."),
    'rail_fence': (rail_fence_cipher,
                   "Rail Fence Cipher: The text is written in a zigzag pattern across multiple 'rails' and read off row by row. Example: 'HELLO WORLD' with 3 rails."),
    'affine': (affine_cipher,
               "Affine Cipher: Each letter is mapped using a linear transformation defined by parameters 'a' and 'b'. Example: 'HELLO' with a=5 and b=8."),
    'custom': (custom_cipher,
               "Custom Cipher: Uses a substitution key defined in a file where each character is mapped to another. Example: 'a' maps to 'w'.")
}


# Основна функція
def main():
    print_intro()  # Show intro with logo and version information

    while True:
        print(Colors.HEADER + "\n--- Cipher Selection Menu ---" + Colors.ENDC)

        # Вибір шифру
        for i, (cipher, _) in enumerate(ciphers.items(), 1):
            print(f"{Colors.OKBLUE}{i}. {cipher}{Colors.ENDC}")

        print("\n0. Exit")
        cipher_choice = int(input(f"{Colors.OKCYAN}Choose a cipher (by number): {Colors.ENDC}")) - 1

        if cipher_choice == -1:
            print(Colors.WARNING + "Exiting program." + Colors.ENDC)
            break

        cipher_name = list(ciphers.keys())[cipher_choice]
        cipher_func, description = ciphers[cipher_name]

        while True:
            print(f"\n{Colors.OKGREEN}Selected Cipher: {cipher_name}{Colors.ENDC}")
            print(f"{Colors.BOLD}Description:{Colors.ENDC} {description}")
            print(f"{Colors.BOLD}Example:{Colors.ENDC}")

            if cipher_name == 'caesar':
                print("  Plaintext: HELLO")
                print("  Shift: 3")
                print("  Encrypted: KHOOR")
            elif cipher_name == 'vigenere':
                print("  Plaintext: HELLO")
                print("  Key: KEY")
                print("  Encrypted: RIJVS")
            elif cipher_name == 'atbash':
                print("  Plaintext: HELLO")
                print("  Encrypted: SVVOL")
            elif cipher_name == 'scytale':
                print("  Plaintext: HELLO WORLD")
                print("  Rails: 3")
                print("  Encrypted: HOLEL WRLD O")
            elif cipher_name == 'vernam':
                print("  Plaintext: HELLO")
                print("  Key: XMCKL")
                print("  Encrypted: \x1f\x0f\x12\x0f\x15")
            elif cipher_name == 'rail_fence':
                print("  Plaintext: HELLO WORLD")
                print("  Rails: 3")
                print("  Encrypted: HOLEL WRDLO ")
            elif cipher_name == 'affine':
                print("  Plaintext: HELLO")
                print("  a: 5, b: 8")
                print("  Encrypted: LIPPS")
            elif cipher_name == 'custom':
                print("  Plaintext: HELLO")
                print("  Key File: custom_key.txt")
                print("  Example Key File Content:")
                print("    a=w")
                print("    b=Y")
                print("  Encrypted: Example output with custom mappings.")

            user_input = input(f"\n{Colors.OKCYAN}Enter '1' to continue or '2' to choose another cipher: {Colors.ENDC}")

            if user_input == '1':
                break
            elif user_input == '2':
                break

        if user_input == '2':
            continue

        # Введення параметрів для шифрів
        args = []
        if cipher_name == 'caesar':
            shift = int(input("Enter shift value: "))
            args.append(shift)
        elif cipher_name == 'vigenere':
            key = input("Enter key: ")
            args.append(key)
        elif cipher_name == 'scytale':
            shift = int(input("Enter shift value: "))
            args.append(shift)
        elif cipher_name == 'vernam':
            key = input("Enter key (same length as text): ")
            args.append(key)
        elif cipher_name == 'rail_fence':
            num_rails = int(input("Enter number of rails: "))
            args.append(num_rails)
        elif cipher_name == 'affine':
            a = int(input("Enter value for 'a': "))
            b = int(input("Enter value for 'b': "))
            args.extend([a, b])
        elif cipher_name == 'custom':
            key_file = input("Enter path to custom key file: ")
            args.append(key_file)

        input_file = input("Enter path to input file: ")
        output_file = input("Enter path to output file: ")

        text = read_text_from_file(input_file)
        encrypted_text = encrypt_text(text, cipher_func, *args)
        write_text_to_file(output_file, encrypted_text)
        print(f"\n{Colors.OKGREEN}Text encrypted using {cipher_name} and saved to {output_file}{Colors.ENDC}")


if __name__ == "__main__":
    main()