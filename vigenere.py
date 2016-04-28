#!/usr/bin/python3
from itertools import cycle,count
import string
import argparse
import fileinput

def decryption_table(alphabet):
  return {k:{c:p for c,p in zip(alphabet[i:]+alphabet[:i],alphabet)} 
            for i,k in zip(count(),alphabet)}

def encryption_table(alphabet):
  return {k:{p:c for c,p in zip(alphabet[i:]+alphabet[:i],alphabet)} 
            for i,k in zip(count(),alphabet)}

def encrypt_decrypt(table,key,text):
  out_text=[table[k][c] for c,k in zip(text,cycle(key))]
  return "".join(out_text)

def decrypt(alphabet,key,cypher_text):
  table=decryption_table(alphabet)
  plain_text=[table[k][c] for c,k in zip(cypher_text,cycle(key))]
  return "".join(plain_text)
      
def prepare(plain_text):
  return "".join(filter(lambda c: c in string.ascii_uppercase,
                        plain_text.upper()))
  #return [c for c in plain_text.upper() if c in string.ascii_uppercase]

if __name__=='__main__':
  parser=argparse.ArgumentParser(description='Vigenere encryption tool')
  key_source_group=parser.add_mutually_exclusive_group()
  key_source_group.add_argument('-k','--key',type=str,#nargs=1,
                                help='Encryption key')
  key_source_group.add_argument('-f','--key-file',type=str,nargs=1,
                                help='Filecontaining encryption key')
  direction=parser.add_mutually_exclusive_group()
  direction.add_argument('-d','--decrypt',action='store_true')
  direction.add_argument('-e','--encrypt',action='store_true')
  parser.add_argument('-a','--alphabet',type=str,nargs='+',default=['upper'],
                      choices=['lower','upper','digits'],
                      help='Characters to support')
  parser.add_argument('-g','--group-size',type=int,nargs=1,default=5,
                      help='Size of code groups. Set 0 for no grouping')
  parser.add_argument('-s','--strip',action='store_true',
                      help='Strip non-encypherable charcters from plain text.')
  #default to stdin?
  parser.add_argument('-t','--text',type=str,nargs='+',help='Text to process')
  args=parser.parse_args()
  print(args)
  alphabets={'upper':string.ascii_uppercase,
             'lower':string.ascii_lowercase,
             'digits':string.digits}
  alphabet="".join([alphabets[a] for a in args.alphabet])
  table=None
  if(args.encrypt):
    table=encryption_table(alphabet)
  else:
    table=decryption_table(alphabet)
  try:
    text="".join(args.text)
    print(encrypt_decrypt(table,args.key,text))
  except(TypeError):
    with fileinput.input() as text:
      print(encrypt_decrypt(table,args.key,text))
