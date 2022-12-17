import random as rand
import numpy as np
import pandas as pd

guns_csv = "data/guns.csv" 
perks_csv = "data/perks.csv"
attachments_csv = "data/attachments.csv"

def switch(op):
    if op in ["primary", "Primary"]:
        print(primary())
    elif op in ["secondary", "Secondary"]:
        print(secondary())
    elif op in ["perks", "Perks", "Perk", "perk"]:
        print(perks())
    else:
        print("Error: Please input Primary, Secondary, or exit")

def random(limit):
    num = rand.randint(0,limit-1)
    return num 

def perks():
    df = pd.read_csv(perks_csv)
    df = df.fillna('-')
    limit = len(df.index)
    perks = []
    for x in range(2):
        num = random(limit)
        perk = df['Basic'].iloc[num]
        perks.append(perk)
    while True:
        num = random(limit)
        perk = df['Bonus'].iloc[num]
        if perk != "-":
            perks.append(perk)
            break
        else:
            continue
    while True:
        num = random(limit)
        perk = df['Ultimate'].iloc[num]
        if perk != "-":
            perks.append(perk)
            break
        else:
            continue
    return perks
    
def primary():
    df = pd.read_csv(guns_csv)
    limit = len(df.index)
    num = random(limit)
    return df['primary'].iloc[num]

def secondary():
    df = pd.read_csv(guns_csv)
    df = df.fillna('-')
    limit = len(df.index)
    while True:
        num = random(limit)
        if df['secondary'].iloc[num] != "-":
            break
        else:
            continue
    return df['secondary'].iloc[num]

def main():
    while True:
        op = input("Input: ")
        if op == 'exit':
            break
        else:
            switch(op) 
  
if __name__ == "__main__":
    main()
