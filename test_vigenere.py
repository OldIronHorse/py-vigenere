#!/usr/bin/python
from unittest import TestCase,main
import string
from vigenere import decryption_table,encryption_table,encrypt_decrypt

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

if __name__=='__main__':
  main()
