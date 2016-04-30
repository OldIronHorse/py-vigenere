#!/usr/bin/python3
from unittest import TestCase,main
import unittest
from unittest.mock import patch
import string
from io import StringIO
from argparse import Namespace
from vigenere import decryption_table,encryption_table,encrypt_decrypt
from vigenere import prepare,strip,code_groups,main

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

class TestMain(TestCase):
  @patch('sys.stdout', new_callable=StringIO)
  def test_encrypt_uppercase_text_as_argument(self,mock_stdout):
    args=Namespace(key='WINDY',alphabet=['upper'],direction='encrypt',
                   strip=True,text=['MARY','HAD','A','LITTLE','LAMB'],
                   group_size=4,key_file=None)
    main(args,[])
    self.assertEqual('IIEB FWLN OGPB YHJW UO\n',mock_stdout.getvalue())

  @patch('sys.stdout', new_callable=StringIO)
  def test_encrypt_uppercase_text_as_argument_no_grouping(self,mock_stdout):
    args=Namespace(key='WINDY',alphabet=['upper'],direction='encrypt',
                   strip=True,text=['MARY','HAD','A','LITTLE','LAMB'],
                   group_size=0,key_file=None)
    main(args,[])
    self.assertEqual('IIEBFWLNOGPBYHJWUO\n',mock_stdout.getvalue())

  @patch('sys.stdout', new_callable=StringIO)
  def test_decrypt_uppercase_text_as_argument_no_grouping(self,mock_stdout):
    args=Namespace(key='WINDY',alphabet=['upper'],direction='decrypt',
                   strip=True,text=['IIEB','FWLN','OGPB','YHJW','UO'],
                   group_size=7,key_file=None)
    main(args,[])
    self.assertEqual('MARYHADALITTLELAMB\n',mock_stdout.getvalue())

  @patch('sys.stdout', new_callable=StringIO)
  @patch('fileinput.input')
  def test_encrypt_uppercase_text_as_file(self,mock_input,mock_stdout):
    mock_input.return_value=StringIO(
        'MARY HAD A LITTLE LAMB\nIT\'S FLEECE WAS WHITE AS SNOW')
    args=Namespace(key='WINDY',alphabet=['upper'],direction='encrypt',
                   strip=True,text=None,group_size=4,key_file=None)
    main(args,['test_plain_text.txt'])
    mock_input.assert_called_once_with(['test_plain_text.txt'])
    self.assertEqual('IIEB FWLN OGPB YHJW UOLR ONYH CYMJ DQSP VWCW AFQM S\n',
                     mock_stdout.getvalue())

  @patch('sys.stdout', new_callable=StringIO)
  @patch('fileinput.input')
  def test_encrypt_uppercase_text_as_redirection(self,mock_input,mock_stdout):
    mock_input.return_value=StringIO(
        'MARY HAD A LITTLE LAMB\nIT\'S FLEECE WAS WHITE AS SNOW')
    args=Namespace(key='WINDY',alphabet=['upper'],direction='encrypt',
                   strip=True,text=None,group_size=4,key_file=None)
    main(args,[])
    mock_input.assert_called_once_with([])
    self.assertEqual('IIEB FWLN OGPB YHJW UOLR ONYH CYMJ DQSP VWCW AFQM S\n',
                     mock_stdout.getvalue())

  #TODO:more test cases for main
  #TODO:file reading and redirection test cases
 
if __name__=='__main__':
  unittest.main()
