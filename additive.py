import argparse

parser=argparse.ArgumentParser(description="The Monoalphabetic Substitution Cipher (Additive Cipher)")
parser.add_argument('-s','--sentence', metavar='', help='Enter a sentence to encrypt/decrypt', required=True)
parser.add_argument('-k','--key',type=int, help='Enter a substitution key to encrypt/decrypt',required=True)
parser.add_argument('-e','--encrypt', help='Encrypts a sentence', action='store_true')
parser.add_argument('-d','--decrypt', help='Decrypts a sentence', action='store_true')
args = parser.parse_args()

# The possible letters in a plaintext 
letters = "abcdefghijklmnopqrstuvwxyz"

# Encryption algorithm
def encrypt(text,key = 3):
    ciphertext = ""
    for letter in text:
        if letter != " ":
            # position of letter in our letters string
            index=letters.find(letter)
            ciphertext += letters[(index+key)%26]
        else:
            ciphertext += " "
    return ciphertext

# Decryption algorithm
def decrypt(text,key = 3):
    plaintext = ""
    for letter in text:
        if letter != " ":
            # position of letter in our letters string
            index=letters.find(letter)
            temp = index - key
            if temp<0:
                temp+=26
                plaintext += letters[temp%26]
            else:
                plaintext += letters[temp%26]
        else:
            plaintext += " "
    return plaintext

if __name__ == '_main_' :
    if args.encrypt:
        print(encrypt(args.sentence,args.key))
    elif args.decrypt:
        print(decrypt(args.sentence,args.key))
    else:
        print("You entered invalid option")
    