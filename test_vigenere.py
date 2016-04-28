#!/usr/bin/python
from unittest import TestCase,main
import string
from vigenere import decryption_table,encryption_table,encrypt_decrypt
from vigenere import prepare

class TestGenerateTable(TestCase):
  def test_encryption_table(self):
    self.assertEqual({'A':{'A':'A','B':'B','C':'C','D':'D'},
                      'B':{'A':'B','B':'C','C':'D','D':'A'},
                      'C':{'A':'C','B':'D','C':'A','D':'B'},
                      'D':{'A':'D','B':'A','C':'B','D':'C'}},
                     encryption_table('ABCD'))

  def test_decyption_table(self):
    self.assertEqual({'A':{'A':'A','B':'B','C':'C','D':'D'},
                      'B':{'A':'D','B':'A','C':'B','D':'C'}, 
                      'C':{'A':'C','B':'D','C':'A','D':'B'}, 
                      'D':{'A':'B','B':'C','C':'D','D':'A'}},
                     decryption_table('ABCD'))


class TestEncryptDecrypt(TestCase):
  def test_encrypt(self):
    table=encryption_table(string.lowercase)
    self.assertEqual('poesadr',
                     encrypt_decrypt(table,'donut','maryhad'))

  def test_decrypt(self):
    table=decryption_table(string.lowercase)
    self.assertEqual('maryhad',
                     encrypt_decrypt(table,'donut','poesadr'))

  def test_encrypt_nonalphabet_characters(self):
    table=encryption_table(string.lowercase)
    self.assertRaises(KeyError,
                      encrypt_decrypt, table,'donut','mary had')

#TODO:charcters not in alphabet?
# best practice helpers: to uppercase, strip whitespace, code groups

class TestPrepare(TestCase):
  def test_prepare(self):
    self.assertEqual('MARYHADALITTLELAMBITSFLEECEWASWHITEASSNOW',
                     prepare("Mary had a little lamb, "+\
                             "it's fleece was white as snow"))

if __name__=='__main__':
  main()
