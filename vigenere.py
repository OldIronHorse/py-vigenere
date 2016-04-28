#!/usr/bin/python
from itertools import cycle,izip,count

def generate_table(alphabet):
  characters=[c for c in alphabet]
  table=[]
  for i in range(len(characters)):
    table.append(characters[i:]+characters[0:i])
  return table

def encrypt(table,key,plain_text):
  c_map={}
  for i,c in izip(count(),table[0]):
    c_map[c]=i
  cypher_text=[]
  for pc,k in izip(plain_text,cycle(key)):
    cypher_text.append(table[c_map[k]][c_map[pc]])
  return "".join(cypher_text)

def decrypt(table,key,cypher_text):
  c_map={}
  for i,c in izip(count(),table[0]):
    c_map[c]=i
  plain_text=[]
  for cc,k in izip(cypher_text,cycle(key)):
    for i,c in izip(count(),table[c_map[k]]):
      if c==cc:
        plain_text.append(table[0][i])
        break
  return "".join(plain_text)
      
