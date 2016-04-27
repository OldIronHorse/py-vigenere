#!/usr/bin/python
from unittest import TestCase, main
from vigenere import generate_table

class TestGenerateTable(TestCase):
  def test_small_alphabet(self):
    self.assertEqual([['A','B','C','D'],
                      ['B','C','D','A'],
                      ['C','D','A','B'],
                      ['D','A','C','C']],
                     generate_table("ABCD"))

if __name__=='__main__':
  main()
