# -*- coding: utf-8 -*-
"""SPCC_EXP_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/173ox8_pGFtSmIZpSesMlS0tdi_tKSYet
"""

import string
import pandas as pd
import numpy as np
import random
import os.path
from csv import writer
from tabulate import tabulate

def take_input():
  print("1 . Create Table  2 . Search Table  3. Enter Symbol 4. Remove Symbol 5. View Table 6 . Exit")
  n = int(input("Enter Your Choice "))
  return n

IDENTIFIERS = list(string.ascii_letters) + ['1','2','3','4','5','6','7','8','9','0']
OPERATORS = ['+' ,'-' , '*','/','=']
INPUT_LIST = []
FILE_NAME = "Table_Data.csv"
COLUMN = ["SYMBOL",'ADDRESS','TYPE']

def create_table():
  print("Creating Table in Progress")
  global INPUT_LIST
  if(len(INPUT_LIST) > 0):
    for expression in INPUT_LIST:
      generate_table(expression)
    
    INPUT_LIST = []
  else:
    print("ENTER EXPRESSION FIRST")

def generate_table(expression):
  letters = [x for x in expression]
  data = {
      "SYMBOL":[],
      "ADDRESS":[],
      "TYPE":[]
  }
  try:
    file_read = pd.read_csv(FILE_NAME,index_col=[0])
    symbols = file_read['SYMBOL'].to_list()
  except FileNotFoundError:
    symbols = []
    pass

  for sym in letters:
    if not (sym in symbols) or len(symbols) == 0 :
      address = id(sym)
      data["ADDRESS"].append(address)
      data["SYMBOL"].append(sym)
      if sym in OPERATORS :
        data["TYPE"].append("operators")
      elif sym in IDENTIFIERS:
        data["TYPE"].append("identifiers")
    else:
      print(f"Sorry Unable To Update Table As {sym} already exits in File ")
      return

  # print(data)
  new_file = pd.DataFrame(data)
    
  try:
    old_file = pd.read_csv(FILE_NAME,index_col=[0])
    df = pd.concat([old_file , new_file], ignore_index= True)
    df.to_csv(FILE_NAME )
    print("SuccessFully Created Table")
  except FileNotFoundError:
    new_file.to_csv(FILE_NAME)
    print("File Created")

# generate_table("a=b+c-d*5")



def enter_input():
  expression = input("Enter Your Expression")
  # INPUT_LIST.append(expression)
  generate_table(expression)



def search_in_table(alphabet):

  try:
    file_read = pd.read_csv(FILE_NAME,index_col=[0])
    result = file_read[file_read['SYMBOL'] == alphabet]
    print(result)
  except FileNotFoundError:
    print("Sorry Couldnt Read File As It Does Not Exist")
    return

# search_in_table("C")

def remove_from_table(alpha):
  try:
    file_read = pd.read_csv(FILE_NAME ,index_col=[0])
    print(file_read['SYMBOL'])
    if alpha in file_read['SYMBOL'].to_list():
      new_file = file_read[file_read['SYMBOL'] != alpha]
      new_file.to_csv(FILE_NAME)
      print(f"{alpha} Removed From Table Data")
    else:
      print(f"{alpha} Does Not Exist in Table Data")
  except FileNotFoundError:
    print("Sorry Couldnt Read File As It Does Not Exist")
    return

# remove_from_table('M')

def view_table():
  try:
    file_read = pd.read_csv(FILE_NAME,index_col=[0])
    print(tabulate(file_read, headers='keys', tablefmt='psql'))
  except FileNotFoundError:
    print("Sorry Couldnt Read File As It Does Not Exist")
    return

# view_table()

while True:
  t = take_input()

  if t == 1 :
    # create table
    create_table()
  elif t == 2:
    #  search in table
    sym = input("Enter Alphabet To Be Searched....")
    search_in_table(sym)
  elif t == 3:
    # Enter Symbol
    enter_input()
  elif t == 4 :
    # Remove Symbo
    sym = input("Enter Symbol To Be Removed From Table")
    remove_from_table(sym)
  elif t == 5:
    # View Table
    view_table()
  elif t == 6:
    break;
  else:
    print("wrong Input")

