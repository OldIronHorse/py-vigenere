#!/usr/bin/python
from itertools import cycle,izip,count
import string

def decryption_table(alphabet):
  return {k:{c:p for c,p in izip(alphabet[i:]+alphabet[:i],alphabet)} 
            for i,k in izip(count(),alphabet)}

def encryption_table(alphabet):
  return {k:{p:c for c,p in izip(alphabet[i:]+alphabet[:i],alphabet)} 
            for i,k in izip(count(),alphabet)}

def encrypt_decrypt(table,key,text):
  out_text=[table[k][c] for c,k in izip(text,cycle(key))]
  return "".join(out_text)

def decrypt(alphabet,key,cypher_text):
  table=decryption_table(alphabet)
  plain_text=[table[k][c] for c,k in izip(cypher_text,cycle(key))]
  return "".join(plain_text)
      
def prepare(plain_text):
  return filter(lambda c: c in string.uppercase,plain_text.upper())
