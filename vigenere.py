#!/usr/bin/python
from itertools import cycle,izip,count

def decryption_table(alphabet):
  return {k:{c:p for c,p in izip(alphabet[i:]+alphabet[:i],alphabet)} 
            for i,k in izip(count(),alphabet)}

def encryption_table(alphabet):
  return {k:{p:c for c,p in izip(alphabet[i:]+alphabet[:i],alphabet)} 
            for i,k in izip(count(),alphabet)}

def encrypt(alphabet,key,plain_text):
  table=encryption_table(alphabet)
  cypher_text=[table[k][p] for p,k in izip(plain_text,cycle(key))]
  return "".join(cypher_text)

def decrypt(alphabet,key,cypher_text):
  table=decryption_table(alphabet)
  plain_text=[table[k][c] for c,k in izip(cypher_text,cycle(key))]
  return "".join(plain_text)
      
