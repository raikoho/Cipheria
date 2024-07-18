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
   .+------+     +------+     +------+     +------+     +------+.
 .' |    .'|    /|     /|     |      |     |\     |\    |`.    | `.
+---+--+'  |   +-+----+ |     +------+     | +----+-+   |  `+--+---+
|   |  |   |   | |    | |     |      |     | |    | |   |   |  |   |
|  ,+--+---+   | +----+-+     +------+     +-+----+ |   +---+--+   |
|.'    | .'    |/     |/      |      |      \|     \|    `. |   `. |
+------+'      +------+       +------+       +------+      `+------+
{Colors.ENDC}
{Colors.OKCYAN}Cipheria Decryptor - tool to decrypt text{Colors.ENDC}
{Colors.OKCYAN}Version 1.0{Colors.ENDC}
{Colors.HEADER}---------------------------------{Colors.ENDC}
""")

# Базові декодувальні функції

def caesar_decipher(text, shift):
    """Decrypts text using Caesar cipher with a given shift."""
    shift = -shift  # Shifting in the opposite direction
    decrypted_text = ''
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - start + shift) % 26 + start)
        else:
            decrypted_text += char
    return decrypted_text

def vigenere_decipher(text, key):
    """Decrypts text using Vigenère cipher with a given key."""
    result = []
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    text_as_int = [ord(i) for i in text]
    for i in range(len(text_as_int)):
        if text[i].isalpha():
            value = (text_as_int[i] - key_as_int[i % key_length]) % 26
            if text[i].isupper():
                result.append(chr(value + 65))
            else:
                result.append(chr(value + 97))
        else:
            result.append(text[i])
    return ''.join(result)

def atbash_decipher(text):
    """Decrypts text using Atbash cipher."""
    return atbash_cipher(text)  # Atbash is symmetric

def atbash_cipher(text):
    """Encrypts or decrypts text using Atbash cipher."""
    decrypted_text = ''
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr(start + (25 - (ord(char) - start)))
        else:
            decrypted_text += char
    return decrypted_text

def scytale_decipher(text, shift):
    """Decrypts text using Scytale cipher with a given shift."""
    n = len(text)
    num_rows = shift
    num_cols = (n + num_rows - 1) // num_rows
    result = [''] * num_cols
    for i in range(num_cols):
        for j in range(num_rows):
            index = i + j * num_cols
            if index < n:
                result[i] += text[index]
    return ''.join(result)

def vernam_decipher(text, key):
    """Decrypts text using Vernam cipher with a given key."""
    decrypted = "".join(chr(ord(char) ^ ord(key[i])) for i, char in enumerate(text))
    return decrypted

def rail_fence_decipher(text, num_rails):
    """Decrypts text using Rail Fence cipher with a given number of rails."""
    rails = [''] * num_rails
    rail = 0
    direction = 1
    for char in text:
        rails[rail] += char
        rail += direction
        if rail == 0 or rail == num_rails - 1:
            direction *= -1

    result = []
    index = 0
    for r in range(num_rails):
        while index < len(rails[r]):
            result.append(rails[r][index])
            index += 1
    return ''.join(result)

def affine_decipher(text, a, b):
    """Decrypts text using Affine cipher with given 'a' and 'b' values."""
    def modular_inverse(a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

    m = 26  # Number of letters in the English alphabet
    a_inv = modular_inverse(a, m)
    decrypted = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            decrypted += chr(((a_inv * (ord(char) - offset - b)) % m) + offset)
        else:
            decrypted += char
    return decrypted

def custom_decipher(text, key_file):
    """Decrypts text using a custom cipher defined in the key file."""
    with open(key_file, 'r', encoding='utf-8') as file:
        key_map = dict(line.strip().split('=') for line in file if '=' in line)
    reverse_key_map = {v: k for k, v in key_map.items()}

    result = ""
    for char in text:
        result += reverse_key_map.get(char, char)  # Replace character if in key, else leave unchanged
    return result

# Функція для зчитування тексту з файлу
def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Функція для запису розшифрованого тексту у файл
def write_text_to_file(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

# Функція для дешифрування тексту
def decrypt_text(text, cipher_func, *args):
    return cipher_func(text, *args)

# Словник шифрів
ciphers = {
    'caesar': (caesar_decipher, "Caesar Cipher: Each letter in the ciphertext is shifted a certain number of places down or up the alphabet. Example: 'D' with a shift of 3 becomes 'A'."),
    'vigenere': (vigenere_decipher, "Vigenère Cipher: Uses a keyword to reverse the shifting of letters in the ciphertext. Example: 'RIJVS' with key 'KEY' becomes 'HELLO'."),
    'atbash': (atbash_decipher, "Atbash Cipher: Each letter of the alphabet is mapped to its reverse. Example: 'SVVOL' becomes 'HELLO'."),
    'scytale': (scytale_decipher, "Scytale Cipher: Text is read in a zigzag pattern across multiple 'rails' and arranged back in original order. Example: 'HOLEL WRLD O' with 3 rails becomes 'HELLO WORLD'."),
    'vernam': (vernam_decipher, "Vernam Cipher: Uses a random key to XOR with the ciphertext. Each letter is decrypted with a corresponding letter in the key."),
    'rail_fence': (rail_fence_decipher, "Rail Fence Cipher: The text is read off in a zigzag pattern across multiple 'rails' to retrieve the original order. Example: 'HOLEL WRDLO ' with 3 rails becomes 'HELLO WORLD'."),
    'affine': (affine_decipher, "Affine Cipher: Each letter is mapped back using the inverse of the linear transformation defined by parameters 'a' and 'b'. Example: 'LIPPS' with a=5 and b=8 becomes 'HELLO'."),
    'custom': (custom_decipher, "Custom Cipher: Uses a substitution key defined in a file where each character is mapped to another. Example: 'a' maps to 'w', decrypts accordingly.")
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
        try:
            cipher_choice = int(input(f"{Colors.OKCYAN}Choose a cipher (by number): {Colors.ENDC}")) - 1
            if cipher_choice < -1 or cipher_choice >= len(ciphers):
                print(Colors.ERROR + "Invalid choice. Please enter a number corresponding to the list." + Colors.ENDC)
                continue
        except ValueError:
            print(Colors.ERROR + "Invalid input. Please enter a valid number." + Colors.ENDC)
            continue

        if cipher_choice == -1:
            print(Colors.WARNING + "Exiting program." + Colors.ENDC)
            break

        cipher_name = list(ciphers.keys())[cipher_choice]
        cipher_func, description = ciphers[cipher_name]

        while True:
            print(f"\n{Colors.OKGREEN}Selected Cipher: {cipher_name}{Colors.ENDC}")
            print(f"{Colors.OKCYAN}Description:{Colors.ENDC}\n{description}\n")
            print(f"{Colors.OKCYAN}Example:{Colors.ENDC}")

            # Show example based on cipher
            if cipher_name == 'caesar':
                print("  Ciphertext: KHOOR")
                print("  Shift: 3")
                print("  Decrypted: HELLO")
            elif cipher_name == 'vigenere':
                print("  Ciphertext: RIJVS")
                print("  Key: KEY")
                print("  Decrypted: HELLO")
            elif cipher_name == 'atbash':
                print("  Ciphertext: SVVOL")
                print("  Decrypted: HELLO")
            elif cipher_name == 'scytale':
                print("  Ciphertext: HOLEL WRLD O")
                print("  Shift: 3")
                print("  Decrypted: HELLO WORLD")
            elif cipher_name == 'vernam':
                print("  Ciphertext: L9O9J")
                print("  Key: 12345")
                print("  Decrypted: HELLO")
            elif cipher_name == 'rail_fence':
                print("  Ciphertext: HOLEL WRDLO ")
                print("  Number of Rails: 3")
                print("  Decrypted: HELLO WORLD")
            elif cipher_name == 'affine':
                print("  Ciphertext: LIPPS")
                print("  a: 5, b: 8")
                print("  Decrypted: HELLO")
            elif cipher_name == 'custom':
                print("  Ciphertext: H9LL0")
                print("  Key File: custom_key.txt")
                print("  Example Key File Content:")
                print("    a=w")
                print("    b=Y")
                print("  Decrypted: HELLO")

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

        try:
            text = read_text_from_file(input_file)
            decrypted_text = decrypt_text(text, cipher_func, *args)
            write_text_to_file(output_file, decrypted_text)
            print(f"\n{Colors.OKGREEN}Text decrypted using {cipher_name} and saved to {output_file}{Colors.ENDC}")
        except Exception as e:
            print(f"{Colors.ERROR}Error: {e}{Colors.ENDC}")


if __name__ == "__main__":
    main()