from tkinter import *
from collections import namedtuple
import sqlite3

#Declarations
Test = Tk()

#Functions
def InsertWeapon():
    #Declarations
    functionDatabase = sqlite3.connect('Python/Concept_Randomizer.db')
    RowStructure = namedtuple('Weapons', 'weaponID')
    functionDatabase.row_factory = lambda cursor, row: RowStructure(*row)
    insertCursor = functionDatabase.cursor()

    #Main
    for item in insertCursor.execute("SELECT weaponID FROM Weapons ORDER BY weaponID DESC LIMIT 1"):
        insertID = item.weaponID

    insertCursor.execute("INSERT INTO Weapons VALUES(:weaponID, :weaponName, :weaponClass)",
        {
            'weaponID': int(insertID) + 1,
            'weaponName': weaponName.get(),
            'weaponClass': weaponClass.get()
        }
    )

    #Closing Args
    functionDatabase.commit()
    functionDatabase.close()
    weaponName.delete(0, END)
    weaponClass.delete(0, END)
    
def InsertCreature():
    #Declarations
    functionDatabase = sqlite3.connect('Python/Concept_Randomizer.db')
    RowStructure = namedtuple('Creatures', 'creatureID')
    functionDatabase.row_factory = lambda cursor, row: RowStructure(*row)
    insertCursor = functionDatabase.cursor()

    #Main
    for creature in insertCursor.execute("SELECT creatureID FROM Creatures ORDER BY creatureID DESC LIMIT 1"):
        insertID = creature.creatureID

    insertCursor.execute("INSERT INTO Creatures VALUES(:creatureID, :creatureName, :creatureClass)",
        {
            'creatureID': int(insertID) + 1,
            'creatureName': creatureName.get(),
            'creatureClass': creatureClass.get()
        }
    )

    #closing Args
    functionDatabase.commit()
    functionDatabase.close()
    creatureName.delete(0, END)
    creatureClass.delete(0, END)

def insertElement():
    #Declarations
    functionDatabase = sqlite3.connect('Python/Concept_Randomizer.db')
    RowStructure = namedtuple('Elementals', 'elementID')
    functionDatabase.row_factory = lambda cursor, row: RowStructure(*row)
    insertCursor = functionDatabase.cursor()

    #Main
    for element in insertCursor.execute("SELECT elementID FROM Elementals ORDER BY elementID DESC LIMIT 1"):
        insertID = element.elementID

    insertCursor.execute("INSERT INTO Elementals VALUES(:elementID, :elementName)",
        {
            'elementID': int(insertID) + 1,
            'elementName': elementName.get()
        }
    )

    #Closing Args
    functionDatabase.commit()
    functionDatabase.close()
    elementName.delete(0, END)

def insertTheme():
    #Declarations
    functionDatabase = sqlite3.connect('Python/Concept_Randomizer.db')
    RowStructure = namedtuple('Themes', 'themeID')
    functionDatabase.row_factory = lambda cursor, row: RowStructure(*row)
    insertCursor = functionDatabase.cursor()

    #Main
    for theme in insertCursor.execute("SELECT themeID FROM Themes ORDER BY themeID DESC LIMIT 1"):
        insertID = theme.themeID

    insertCursor.execute("INSERT INTO Themes VALUES(:themeID, :themeName)",
        {
            'themeID': int(insertID) + 1,
            'themeName': themeName.get()
        }
    )

    #Closing Args
    functionDatabase.commit()
    functionDatabase.close()
    themeName.delete(0, END)

#Widgets
#Weapon
weaponName = Entry(Test, width = 20)
weaponClass = Entry(Test, width = 20)
weaponNameLabel = Label(Test, text = 'Weapon Name: ')
weaponClassLabel = Label(Test, text = 'Weapon Class: ')
weaponButtonInsert = Button(Test, text = 'Insert', command = InsertWeapon)
#Creature
creatureName = Entry(Test, width = 20)
creatureClass = Entry(Test, width = 20)
creatureNameLabel = Label(Test, text = 'Creature Name: ')
creatureClassLabel = Label(Test, text = 'Creature Class: ')
creatureButtonInsert = Button(Test, text = 'Insert', command = InsertCreature)
#Buffer
bufferLabelOne = Label(Test)
bufferLabelTwo = Label(Test, text = '   ')
#Elements
elementName = Entry(Test, width = 20)
elementNameLabel = Label(Test, text = 'Element Name: ')
elementButtonInsert = Button(Test, text = 'Insert', command = insertElement)
#Themes
themeName = Entry(Test, width = 20)
themeNameLabel = Label(Test, text = 'Theme Name: ')
themeButtonInsert = Button(Test, text = 'Insert', command = insertTheme)

#Adding to Screen
weaponNameLabel.grid(row = 0, column = 0)
weaponClassLabel.grid(row = 1, column = 0)
weaponName.grid(row = 0, column = 1)
weaponClass.grid(row = 1, column = 1)

creatureNameLabel.grid(row = 0, column = 4)
creatureClassLabel.grid(row = 1, column = 4)
creatureName.grid(row = 0, column = 5)
creatureClass.grid(row = 1, column = 5)

bufferLabelOne.grid(row = 3, column = 0)
bufferLabelTwo.grid(row = 0, column = 3)

elementNameLabel.grid(row = 4, column = 0)
elementName.grid(row = 4, column = 1)

themeNameLabel.grid(row = 4, column = 4)
themeName.grid(row = 4, column = 5)

weaponButtonInsert.grid(row = 2, column = 0, columnspan = 2, sticky = 'we')
creatureButtonInsert.grid(row = 2, column = 4, columnspan = 2, sticky = 'we')
elementButtonInsert.grid(row = 5, column = 0, columnspan = 2, sticky = 'we')
themeButtonInsert.grid(row = 5, column = 4, columnspan = 2, sticky = 'we')

#Closing Args
Test.mainloop()