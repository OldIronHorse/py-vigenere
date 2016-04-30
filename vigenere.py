#!/usr/bin/python3
from itertools import cycle,count
import string
import argparse
import fileinput
import sys

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

def strip(alphabet,text):
  return "".join(filter(lambda c: c in alphabet, text))

def code_groups(size,text):
  if size==0:
    return text
  groups=[]
  group=[]
  for i,c in zip(count(),text):
    group.append(c)
    if len(group)==size:
      groups.append(''.join(group))
      group=[]
  groups.append(''.join(group))
  return ' '.join(groups)

def main(args,unknown):
  alphabets={'upper':string.ascii_uppercase,
             'lower':string.ascii_lowercase,
             'digits':string.digits,
             'space':' '}
  table_fns={'encrypt':encryption_table,
             'decrypt':decryption_table}
  alphabet="".join([alphabets[a] for a in args.alphabet])
  table=table_fns[args.direction](alphabet)
  text=''
  try:
    text=''.join(args.text)
  except(TypeError):
    lines=[]
    with fileinput.input(unknown) as f:
      for line in f:
        lines.append(line)
    text=''.join(lines)
  if(args.strip):
    text=strip(alphabet,text)
  out_text=encrypt_decrypt(table,args.key,text)
  if(args.direction=='encrypt'):
    out_text=code_groups(args.group_size,out_text)
  print(out_text)

if __name__=='__main__':
  parser=argparse.ArgumentParser(description='Vigenere encryption tool')
  key_source_group=parser.add_mutually_exclusive_group()
  key_source_group.add_argument('-k','--key',type=str,
                                help='Encryption key')
  key_source_group.add_argument('-f','--key-file',type=str,nargs=1,
                                help='Filecontaining encryption key')
  parser.add_argument('-d','--direction',type=str,default='encrypt',
                      choices=['encrypt','decrypt'])
  parser.add_argument('-a','--alphabet',type=str,nargs='+',default=['upper'],
                      choices=['lower','upper','digits','space'],
                      help='Characters to support')
  parser.add_argument('-g','--group-size',type=int,nargs=1,default=5,
                      help='Size of code groups. Set 0 for no grouping')
  parser.add_argument('-s','--strip',action='store_true',
                      help='Strip non-encypherable charcters from plain text.')
  parser.add_argument('-t','--text',type=str,nargs='+',help='Text to process')
  args,unknown=parser.parse_known_args()
  main(args,unknown)
