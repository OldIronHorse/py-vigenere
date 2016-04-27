#!/usr/bin/python

def generate_table(alphabet):
  characters=[c for c in alphabet]
  table=[]
  for i in range(len(characters)):
    table.append(characters[i:]+characters[0:i])
  return table
