#!/usr/bin/python
from itertools import cycle,izip,count

def generate_table(alphabet):
  return[alphabet[i:]+alphabet[0:i] for i in range(len(alphabet))]

def encrypt(alphabet,key,plain_text):
  table=generate_table(alphabet)
  c_map={c: i for i,c in izip(count(),table[0])}
  cypher_text=[table[c_map[k]][c_map[pc]]
               for pc,k in izip(plain_text,cycle(key))]
  return "".join(cypher_text)

def decrypt(alphabet,key,cypher_text):
  table=generate_table(alphabet)
  c_map={c: i for i,c in izip(count(),table[0])}
  plain_text=[]
  for cc,k in izip(cypher_text,cycle(key)):
    for i,c in izip(count(),table[c_map[k]]):
      if c==cc:
        plain_text.append(table[0][i])
        break
  return "".join(plain_text)
      
