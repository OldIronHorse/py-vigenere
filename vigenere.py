#!/usr/bin/python
from itertools import cycle,izip,count
import string

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

def decrypt(table,key,cypher_text):
  c_map={}
  i=0
  for c in table[0]:
    c_map[c]=i
    i+=1
  plain_text=[]
  for cc,k in izip(cypher_text,cycle(key)):
    for i,c in izip(count(),table[c_map[k]]):
      if c==cc:
        plain_text.append(table[0][i])
        break
  return "".join(plain_text)
      
def prepare(plain_text):
  return filter(lambda c: c in string.uppercase,plain_text.upper())
