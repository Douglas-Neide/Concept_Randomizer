from tkinter import *
from collections import namedtuple
import sqlite3
import random

#Main Window
window = Tk()
functionDatabase = sqlite3.connect('Python/Concept_Randomizer.db')

#Generating Lists
weaponList = []
creatureList = []
elementList = []
themeList = []

RowStructure = namedtuple('Weapons', 'weaponName')
functionDatabase.row_factory = lambda cursor, row: RowStructure(*row)
for weapon in functionDatabase.execute("SELECT weaponName FROM Weapons"):
    weaponList.append(weapon.weaponName)

RowStructure = namedtuple('Creatures', 'creatureName')
for creature in functionDatabase.execute("SELECT creatureName FROM Creatures"):
    creatureList.append(creature.creatureName)

RowStructure = namedtuple('Elementals', 'elementName')
for elementals in functionDatabase.execute("SELECT elementName FROM Elementals"):
    elementList.append(elementals.elementName)

RowStructure = namedtuple('Themes', 'themeName')
for theme in functionDatabase.execute("SELECT themeName FROM Themes"):
    themeList.append(theme.themeName)

#Functions
def GenerateWeapon():
    randomWeapon.delete(0, END)
    randTheme = random.choice(themeList)
    randWeap = random.choice(weaponList)
    randElem = random.choice(elementList)
    randOne = hex(themeList.index(randTheme)+1).lstrip('0x')
    randTwo = hex(weaponList.index(randWeap)+1).lstrip('0x')
    randThr = hex(elementList.index(randElem)+1).lstrip('0x')
    if themeList.index(randTheme) < 16:
        randOne = str(0) + randOne
    if weaponList.index(randWeap) < 16:
        randTwo = str(0) + randTwo
    if elementList.index(randElem) < 16:
        randThr = str(0) + randThr
    randID = randOne + randTwo + randThr
    randomWeapon.insert(0, randTheme + ' ' + randWeap + ' of the ' + randElem + ' - ' + randID)

def GenerateCreature():
    randomCreature.delete(0, END)
    randCreat = random.choice(creatureList)
    randElem = random.choice(elementList)
    randOne = hex(creatureList.index(randCreat)+1).lstrip('0x')
    randTwo = hex(elementList.index(randElem)+1).lstrip('0x')
    if creatureList.index(randCreat) < 16:
        randOne = str(0) + randOne
    if elementList.index(randElem) < 16:
        randTwo = str(0) + randTwo
    randID = randOne + randTwo
    randomCreature.insert(0, randCreat + ' of the ' + randElem + ' - ' + randID)

def GenerateHybrid():
    randomHybrid.delete(0, END)
    randCreatOne = random.choice(creatureList)
    randCreatTwo = random.choice(creatureList)
    randElem = random.choice(elementList)
    randOne = hex(creatureList.index(randCreatOne)+1).lstrip('0x')
    randTwo = hex(creatureList.index(randCreatTwo)+1).lstrip('0x')
    randThr = hex(elementList.index(randElem)+1).lstrip('0x')
    if creatureList.index(randCreatOne) < 16:
        randOne = str(0) + randOne
    if creatureList.index(randCreatTwo) < 16:
        randTwo = str(0) + randTwo
    if elementList.index(randElem) < 16:
        randThr = str(0) + randThr
    randID = randOne + randTwo + randThr
    randomHybrid.insert(0, randCreatOne + ' ' + randCreatTwo + ' of the ' + randElem + ' - ' + randID)
    
def EditList():
    exec(open('Python/DatabasePractice.py').read())
    

#Widgets
randomWeapon = Entry(window, width = 50, borderwidth = 5)
randomCreature = Entry(window, width = 50, borderwidth = 5)
randomHybrid = Entry(window, width = 50, borderwidth = 5)

rollWeaponButton = Button(window,text = 'Generate Weapon', command = GenerateWeapon)
rollCreatureButton = Button(window, text = 'Generate Creature', command = GenerateCreature)
rollHybridButton = Button(window, text = 'Generate Hybrid', command = GenerateHybrid)

editLists = Button(window, text = 'Edit Lists', command = EditList)
exitButton = Button(window, text = 'Close', command = exit)

rollWeaponButton.grid(row = 0, column = 0, sticky = "we")
rollCreatureButton.grid(row = 1, column = 0, sticky = "we")
rollHybridButton.grid(row = 2, column = 0, sticky = "we")
editLists.grid(row = 3, column = 0, sticky = "we")

randomWeapon.grid(row = 0, column = 1)
randomCreature.grid(row = 1, column = 1)
randomHybrid.grid(row = 2, column = 1)
exitButton.grid(row = 3, column = 1, sticky = "e")

#ClosingArgs
window.mainloop()
functionDatabase.commit()
functionDatabase.close()