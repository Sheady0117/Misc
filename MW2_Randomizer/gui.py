import random as rand
import numpy as np
import pandas as pd
import PySimpleGUI as sg

guns_csv = "data/guns.csv" 
perks_csv = "data/perks.csv"
attachments_csv = "data/attachments.csv"

def random(limit):
    num = rand.randint(0,limit-1)
    return num 

def loadout():
    loadout = primary()
    loadout = loadout.append(secondary())
    loadout = loadout.append(perks())

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
    sg.theme('DarkGrey6')
    layout = [
        [sg.Button('Primary'), sg.Button('Secondary'), sg.Button('Perks')],
        [sg.Button('Loadout')],
        [sg.Text(size=(0,1), key='Space')],
        [sg.Text(size=(0,1), key='OUTPUT')],
        [sg.Text(size=(0,1), key='OUTPUT1')],
        [sg.Text(size=(0,1), key='OUTPUT2')],
           
    ]
    
    window = sg.Window("Modern Warfare 2 Loadout Randomizer", layout, element_justification='c')
    #Figure out how to center layout and make size right size=(500,300)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Primary':
            window['OUTPUT'].update(value=primary())
            window['OUTPUT1'].update(value='')
            window['OUTPUT2'].update(value='') 
            
        if event == 'Secondary':
            window['OUTPUT'].update(value=secondary())
            window['OUTPUT1'].update(value='')
            window['OUTPUT2'].update(value='')
        if event == 'Perks':
            window['OUTPUT'].update(value=perks())
            window['OUTPUT1'].update(value='')
            window['OUTPUT2'].update(value='')
        if event == 'Loadout':
            window['OUTPUT'].update(value=primary())
            window['OUTPUT1'].update(value=secondary())
            window['OUTPUT2'].update(value=perks())  
if __name__ == "__main__":
    main()
