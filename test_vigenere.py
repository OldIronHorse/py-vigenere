#!/usr/bin/python
from unittest import TestCase,main
import string
from vigenere import generate_table,encrypt,decrypt

class TestGenerateTable(TestCase):
  def test_small_alphabet(self):
    self.assertEqual(['ABCD',
                      'BCDA',
                      'CDAB',
                      'DABC'],
                     generate_table("ABCD"))


class TestEncryptDecrypt(TestCase):
  def setUp(self):
    self.table=generate_table(string.lowercase)

  def test_encrypt(self):
    self.assertEqual('poesadr',
                     encrypt(string.lowercase,'donut','maryhad'))

  def test_decrypt(self):
    self.assertEqual('maryhad',
                     decrypt(string.lowercase,'donut','poesadr'))

if __name__=='__main__':
  main()
