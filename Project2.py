# File: Project2.py
# Student: Ruijia Huang
# UT EID: rh38477
# Course Name: CS303E
# 
# Date Created: 11/7/2021
# Date Last Modified: 11/8/2021
# Description of Program: The program has methods to assist with the encryption and decryption of substitution cyphers. The program automatically
# creates a random key if none is given to an object. The class can return the key, change the key if it's legal, and encrypt/decrypt the text given
# according to the key in the substitution cipher object. The main function uses this class to nicely format the returned strings.

import random

# A global constant defining the alphabet. 
LCLETTERS = "abcdefghijklmnopqrstuvwxyz"

def isLegalKey( key ):
    # A key is legal if it has length 26 and contains all letters.
    # from LCLETTERS.
    return ( len(key) == 26 and all( [ ch in key for ch in LCLETTERS ] ) )

def makeRandomKey():
    # A legal random key is a permutation of LCLETTERS.
    lst = list( LCLETTERS )  # Turn string into list of letters
    random.shuffle( lst )    # Shuffle the list randomly
    return ''.join( lst )    # Assemble them back into a string

class SubstitutionCipher:
    def __init__(self, key = makeRandomKey()):
        self.__key = key

    def getKey(self):
        return self.__key
    
    def setKey(self, newKey):
        if(isLegalKey(newKey)):
            self.__key = newKey
        else:
            print("Key entered is not legal")

    def encryptText(self, plainText):
        encrypted = ""
        for i in range(len(plainText)):
            if(plainText[i].isupper() == True):
                ch = plainText[i].lower()
                index = ord(ch) - 97
                upperCh = (self.__key[index]).upper()
                encrypted += upperCh
            elif(ord(plainText[i].lower()) > 122 or ord(plainText[i].lower()) < 97):
                encrypted += plainText[i]
            else:
                index = ord(plainText[i]) - 97
                encrypted += self.__key[index]
                
        return encrypted

    def decryptText(self, cipherText):
        decrypted = ""
        index = -1
        for i in range(len(cipherText)):
            if(cipherText[i].isupper() == True):
                
                ch = cipherText[i].lower()

                for o in range(len(self.__key)):
                    if ch == self.__key[o]:
                        index = o
                    else:
                        continue
                upperCh = (LCLETTERS[index]).upper()
                decrypted += upperCh

            elif(ord(cipherText[i].lower()) > 122 or ord(cipherText[i].lower()) < 97):
                decrypted += cipherText[i]
            else:
                for o in range(len(self.__key)):
                    if cipherText[i] == self.__key[o]:
                        index = o
                    else:
                        continue
                decrypted += LCLETTERS[index]
                
        return decrypted

def main():
    cipher = SubstitutionCipher()
    while(True):
        comm = input("Enter a command (getKey, changeKey, encrypt, decrypt, quit): ")
        comm = comm.lower()

        if(comm == "getkey"):
            print("\tCurrent cipher key:", cipher.getKey())
        elif(comm == "changekey"):
            while(True):
                newCipher = input("\tEnter a valid cipher key, 'random' for a random key, or 'quit' to quit: ")
                if(newCipher == "random"):
                    cipher.setKey(makeRandomKey())
                    print("\t\tNew cipher key:", cipher.getKey())
                    break
                elif(newCipher == "quit"):
                    break
                else:
                    if(isLegalKey(newCipher)):
                        cipher.setKey(newCipher)
                        break
                    else:
                        print("\t\tIllegal key entered. Try again!")
        elif(comm == "encrypt"):
            plain = input("\tEnter a text to encrypt: ")
            encrypted = cipher.encryptText(plain)
            print("\t\tThe encrypted text is", encrypted)
        elif(comm == "decrypt"):
            decrypt = input("\tEnter a text to decrypt: ")
            plain = cipher.decryptText(decrypt)
            print("\t\tThe decrypted text is:", plain)
        elif(comm == "quit"):
            print("Thanks for visiting!")
            break
        else:
            print("\tCommand not recognized. Try again!")

main()