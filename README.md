# Cipheria

![Cipheria Logo](https://your-image-link-here.com/logo.png)
Secure your text with elegance and simplicity

**Version 1.0**

Cipheria is a powerful yet easy-to-use suite of text encryption and decryption tools, designed to help you secure your messages with a variety of classic and custom ciphers. This repository contains two Python programs: an encoder and a decoder, capable of working with multiple encryption algorithms.

## Features

- **Caesar Cipher**
- **Vigenère Cipher**
- **Atbash Cipher**
- **Scytale Cipher**
- **Vernam Cipher**
- **Rail Fence Cipher**
- **Affine Cipher**
- **Custom Substitution Cipher**

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
  - [Encoder](#encoder)
  - [Decoder](#decoder)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Cipheria allows you to encode and decode text files using a variety of encryption methods. Whether you are looking to secure sensitive information or just want to experiment with classical ciphers, Cipheria offers a range of tools to meet your needs.

## 🛠️Installation and Start
```sh
git clone https://github.com/raikoho/Cipheria.git
cd Cipheria
pip install -r requirements.txt
python CipheriaEncoder.py
python CipheriaDecoder.py
```
## 🚀Usage
### Encoder
The encoder program allows you to encrypt text files using one of the supported ciphers.

Run the encoder:
```sh
python CipheriaEncoder.py
```

### Decoder
The decoder program allows you to decrypt text files that were encrypted using the encoder program.

Run the decoder:
```sh
python CipheriaDecoder.py
```

### 🔐Custom Cipher
The custom substitution cipher allows you to define your own substitution rules for each character. This is done using a key file (custom_key.txt).

### 🗝️Creating a Custom Key File
The key file should be a text file where each line defines a substitution in the format original=replacement. Write and replace any symbols and letters, use different cases. For example:
```sh
a=w
b=Y
c=9
d=k
1=Q
2=r
...
```
Use the same key-file again to decode the text.

## 👩‍💻Examples

### Encoding Example

1) Select the cipher (e.g., Caesar Cipher)
2) Enter the shift value (e.g., 3)
3) Enter the path to the input file (e.g., input.txt)
4) Enter the path to the output file (e.g., encoded.txt)

####   Sample Input (input.txt):
    HELLO WORLD
####   Sample Output (encoded.txt):
    KHOOR ZRUOG

### Decoding Example

1) Select the cipher (e.g., Caesar Cipher)
2) Enter the shift value (e.g., 3)
3) Enter the path to the input file (e.g., encoded.txt)
4) Enter the path to the output file (e.g., decoded.txt)

####   Sample Input (encoded.txt):
    KHOOR ZRUOG
####   Sample Output (decoded.txt):
    HELLO WORLD

## 📦Contributing
I am welcome contributions from the community! If you have an idea for a new feature, or have found a bug, please open an issue or submit a pull request.

## 📜License
This project is licensed under the MIT License. See the LICENSE file for details.

## 📝Contact
For any questions or suggestions, feel free to reach out to me on LinkedIn or open an issue on GitHub.
