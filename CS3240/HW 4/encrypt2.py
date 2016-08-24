#BORROWED AND MODIFIED FROM CNOX.PY AVAILABLE AT:
#https://github.com/nafscript/cnox/blob/master/cnox.py

import os
import struct

from Crypto.Cipher import AES
from Crypto import Random


block = AES.block_size #16

# Encryption
def Encrypt(in_file, key, out_file=None, chunksize=8192):
    if not out_file:
        out_file = in_file + '.enc'

    iv = Random.new().read(AES.block_size)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_file)

    with open(in_file, 'rb') as infile:
        with open(out_file, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    add = b' ' * (16 - len(chunk)%16)
                    chunk = chunk + add

                outfile.write(encryptor.encrypt(chunk))
    os.remove(in_file)

# Decryption
def Decrypt(in_file, key, out_file=None, chunksize=8192):

    if not out_file:
        out_file = os.path.splitext(in_file)[0]

    with open(in_file, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_file, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(origsize)


def main():
    aesKey = Random.new().read(block)
    Encrypt(in_file="Evatran_journal.docx", key=aesKey)
    Decrypt(in_file="Evatran_journal.docx.enc", key=aesKey)

if __name__ == '__main__':
    main()