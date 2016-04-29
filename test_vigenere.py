#!/usr/bin/python3
from unittest import TestCase,main
import string
from vigenere import decryption_table,encryption_table,encrypt_decrypt
from vigenere import prepare,strip,code_groups

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
    table=encryption_table(string.ascii_lowercase)
    self.assertEqual('poesadr',
                     encrypt_decrypt(table,'donut','maryhad'))

  def test_decrypt(self):
    table=decryption_table(string.ascii_lowercase)
    self.assertEqual('maryhad',
                     encrypt_decrypt(table,'donut','poesadr'))

  def test_encrypt_nonalphabet_characters(self):
    table=encryption_table(string.ascii_lowercase)
    self.assertRaises(KeyError,
                      encrypt_decrypt, table,'donut','mary had')

#TODO:charcters not in alphabet?
# best practice helpers: to uppercase, strip whitespace, code groups

class TestPrepare(TestCase):
  def test_prepare(self):
    self.assertEqual('MARYHADALITTLELAMBITSFLEECEWASWHITEASSNOW',
                     prepare("Mary had a little lamb, "+\
                             "it's fleece was white as snow"))


class TestStrip(TestCase):
  def test_strip_empty_text(self):
    self.assertEqual("",strip("ABCD",""))

  def test_strip(self):
    self.assertEqual("MHALL",
                     strip(string.ascii_uppercase,'Mary Had A Little Lamb,'))

class TestCodeGroups(TestCase):
  def test_zero_length_groups(self):
    cypher_text='ghfkgshdlhkgkdfgh'
    self.assertEqual(cypher_text,code_groups(0,cypher_text))

  def test_nonzero_length_groups(self):
    cypher_text='ghfkgshdlhkgkdfgh'
    self.assertEqual('ghfk gshd lhkg kdfg h',code_groups(4,'ghfkgshdlhkgkdfgh'))

if __name__=='__main__':
  main()
