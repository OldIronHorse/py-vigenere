#!/usr/bin/python
from unittest import TestCase,main
import string
from vigenere import generate_table,encrypt,decrypt

class TestGenerateTable(TestCase):
  def test_small_alphabet(self):
    self.assertEqual([['A','B','C','D'],
                      ['B','C','D','A'],
                      ['C','D','A','B'],
                      ['D','A','B','C']],
                     generate_table("ABCD"))


class TestEncryptDecrypt(TestCase):
  def setUp(self):
    self.table=generate_table(string.lowercase)

  def test_encrypt(self):
    self.assertEqual('poesadr',
                     encrypt(self.table,'donut','maryhad'))

  def test_decrypt(self):
    self.assertEqual('maryhad',
                     decrypt(self.table,'donut','poesadr'))

if __name__=='__main__':
  main()
