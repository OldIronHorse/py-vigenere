#!/usr/bin/python
from itertools import cycle,izip

def generate_table(alphabet):
  characters=[c for c in alphabet]
  table=[]
  for i in range(len(characters)):
    table.append(characters[i:]+characters[0:i])
  return table

def encrypt(table,key,plain_text):
  c_map={}
  i=0
  for c in table[0]:
    c_map[c]=i
    i+=1
  cypher_text=[]
  for pc,k in izip(plain_text,cycle(key)):
    cypher_text.append(table[c_map[k]][c_map[pc]])
  return "".join(cypher_text)
