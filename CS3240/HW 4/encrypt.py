__author__ = 'Reid'

from Crypto.Cipher import AES
from Crypto import Random

import codecs

block = AES.block_size #16
size = 16*1024 #size for reading files

""" used to pad the string with spaces to fit in 16 byte blocks """
def pad(string):
    return string + (block - len(string) % block) * chr(block - len(string) % block)

""" used to unpad the string of spaces """
def unpad(string):
    return string[:-ord(string[len(string) - 1:])]

""" decrypts string with key then returns resulted string """
def decrypt_string(stringEnc, keyU):
    iv = stringEnc[:block]
    cipher = AES.new(keyU, AES.MODE_CBC, iv)
    stringDec = unpad(cipher.decrypt(stringEnc))[block:]
    stringDec = bytes.decode(stringDec)
    return stringDec

""" encrypts string with key, then returns resulted string """
def secret_string(string, keyU):
    pString = pad(string)
    iv = Random.new().read(block)
    cipher = AES.new(keyU, AES.MODE_CBC, iv)
    stringEnc = iv + cipher.encrypt(pString)
    return stringEnc

""" Use symmetric key encryption to encrypt file """
def encrypt_file(filename, keyS):
    filenameOut = filename + '.enc'
    iv = Random.new().read(block)
    cipher = AES.new(keyS, AES.MODE_CBC, iv)
    try:
        f = open(filename, 'rb')
        f.close()
    except:
        print("\tFile not found!")
        return False
    with open(filename, 'rb') as fileIn:
        with open(filenameOut, 'wb') as fileOut:
            print("\tEncrypting " + filename + " to " + filenameOut)
            fileOut.write(iv)
            while True:
                read = fileIn.read(size)
                if len(read) == 0:
                    break
                read = pad(bytes.decode(read))
                fileOut.write(cipher.encrypt(read))
    return True

""" Open the file and decrypts it with the symmetric key """
def decrypt_file(filename, keyS):
    try:
        if filename[-4:] != ".enc":
            print("\t" + filename + " did not end with .enc")
            return False
    except:
        print("\tFile not found!")
        return False
    filenameOut = 'DEC_' + filename[:-4]
    try:
        f = open(filename, 'rb')
        f.close()
    except:
        print("\tFile not found!")
        return False
    with open(filename, 'rb') as fileIn:
        print("\tDecrypting " + filename + " to " + filenameOut)
        iv = fileIn.read(16)
        cipher = AES.new(keyS, AES.MODE_CBC, iv)
        with open(filenameOut, 'wb') as fileOut:
            while True:
                read = fileIn.read(size)
                if len(read) == 0:
                    break
                read = unpad(cipher.decrypt(read))
                fileOut.write(read)
    return True

def main():
    print("TEST 1:")
    aesKey1 = Random.new().read(block)
    print("Creating new AES Key:")
    print("\t" + str(aesKey1))
    string1 = "Hello World!"
    sEnc1 = secret_string(string1, aesKey1)
    print("Encrypting string of length less than 16:")
    print("\t" + str(sEnc1))
    sDec1 = decrypt_string(sEnc1, aesKey1)
    print("Decrypting string of length less than 16:")
    print("\t" + str(sDec1))
    assert(sDec1 == string1)
    print("Complete!")
    print("\n")

    print("TEST 2:")
    aesKey2 = Random.new().read(block)
    print("Creating new AES Key:")
    print("\t" + str(aesKey2))
    string2 = "Hello World! Hi!"
    sEnc2 = secret_string(string2, aesKey2)
    print("Encrypting string of length 16:")
    print("\t" + str(sEnc2))
    sDec2 = decrypt_string(sEnc2, aesKey2)
    print("Decrypting string of length 16:")
    print("\t" + str(sDec2))
    assert (sDec2 == string2)
    print("Complete!")
    print("\n")

    print("TEST 3:")
    aesKey3 = Random.new().read(block)
    print("Creating new AES Key:")
    print("\t" + str(aesKey3))
    string3 = "Hello World! Hi! Bye!"
    sEnc3 = secret_string(string3, aesKey3)
    print("Encrypting string of length more than 16:")
    print("\t" + str(sEnc3))
    sDec3 = decrypt_string(sEnc3, aesKey3)
    print("Decrypting string of length more than 16:")
    print("\t" + str(sDec3))
    assert (sDec3 == string3)
    print("Complete!")
    print("\n")

    print("TEST 4:")
    aesKey4 = Random.new().read(block)
    print("Creating new AES Key:")
    print("\t" + str(aesKey4))
    string4 = ""
    sEnc4 = secret_string(string4, aesKey4)
    print("Encrypting string of length 0:")
    print("\t" + str(sEnc4))
    sDec4 = decrypt_string(sEnc4, aesKey4)
    print("Decrypting string of length 0:")
    print("\t" + str(sDec4))
    assert (sDec4 == string4)
    print("Complete!")
    print("\n")

    print("TEST 5:")
    aesKey5 = Random.new().read(block)
    print("Creating new AES Key:")
    print("\t" + str(aesKey5))
    print("Testing on actual test files that will work")
    encrypt_file("CS_2150_Notes.docx",aesKey5)
    decrypt_file("CS_2150_Notes.docx.enc",aesKey5)
    print("Complete!")
    print("\n")

    print("TEST 6:")
    aesKey6 = Random.new().read(block)
    print("Creating new AES Key:")
    print("\t" + str(aesKey6))
    print("Testing encrypt_file on unavailable text file")
    encrypt_file("notfound.txt", aesKey6)
    print("Complete!")
    print("\n")


    print("TEST 7:")
    aesKey7 = Random.new().read(block)
    print("Creating new AES Key:")
    print("\t" + str(aesKey7))
    print("Testing decrypt_file on unavailable .enc file")
    decrypt_file("notfound.txt.enc", aesKey7)
    print("Complete!")
    print("\n")

    print("TEST 8:")
    aesKey8 = Random.new().read(block)
    print("Creating new AES Key:")
    print("\t" + str(aesKey8))
    print("Testing decrypt_file on file with wrong ending")
    decrypt_file("notfound.txt.ecn", aesKey8)
    print("Complete!")
    print("\n")

    print("TEST 9:")
    aesKey9 = Random.new().read(block)
    print("Creating new AES Key:")
    print("\t" + str(aesKey9))
    print("Testing encrypt_file and decrypt_file on file other than text file")
    encrypt_file("test2.html", aesKey9)
    decrypt_file("test2.html.enc", aesKey9)
    print("Complete!")
    print("\n")

    print("TEST 10:")
    aesKey10 = Random.new().read(block)
    print("Creating new AES Key:")
    print("\t" + str(aesKey10))
    print("Testing decrypt_file with file name less than 4 as well as only being .enc")
    decrypt_file(".enc", aesKey10)
    decrypt_file("hi", aesKey10)
    print("Complete!")
    print("\n")
    
    return 0

if __name__ == "__main__":
    main()
