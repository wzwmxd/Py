# -*- coding=utf-8 -*-
import sys
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


class prpcrypt():
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC

    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        length = 16
        count = len(text)
        add = length - (count % length)
        text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        return b2a_hex(self.ciphertext)

    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip('\0')


if __name__ == '__main__':
    param = sys.argv[1]
    source = sys.argv[2]
    key = sys.argv[3]

    pc = prpcrypt(key)
    infile = open(source, 'r')
    if param == '-e':
        outfile = open(source + '.aes', 'w')
        print >> outfile, pc.encrypt(infile.read())
    else:
        suffix = source.split('.')[-2]
        outfile = open(source + '.' + suffix, 'w')
        print >> outfile, pc.decrypt(infile.read())
