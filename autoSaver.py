'''
This program's main purpose is to save calcs run by TODC and name them as per list of names in 'runway'

There are also some functions to choose what file names appear in runway (the contents of runway must match the TODC calculations):
1. You can update 'runway' with names listed in the file 'runways6.txt' using runwayUpdate() or clicking 'import Runways6'. (manually type names into Runways6, click import Runways6 and then click 'Start save-clicker for TODC Calculation')
2. You can remove any airfeilds not listed in in Airfeilds6.txt from runway using airfeildsUpdae() or clicking 'remove all airfeilds execpt those in Airfeilds6'
4. runways6.txt can be updated with all runways intersections in the latest TODC AODB using runways6Update

Limitations:
This program DOES NOT look for the 'save' pop up, or change the folder where files get saved. It will only save if pop up is in correct location (top RHC of pop up is in top RHC of screen) and there is a non white background under the pop up
This program does ajust for screen size

How to use this program:
Step 1) Make contents of runway variable equal to list of calculations to be run in TODC. There are two ways to do this.
        a) Manually:
           1) Type desired filenames into Runways6.txt in the same order calculations will be run.
           2) Save Runways6.txt
           3) Run runwayUpdate() to import
        b) From AODB:
           1) Import all runway intersections in latest TODC AODB into runways using runways6Update()
           2) optional: remove Airfeilds that are not needed
                      i)    type 4 letter code of airfeilds you want to do calcs on in file Airfieds6.txt.
                      ii)   Save Airfeilds6.txt
                      iii)  Run AirfeildsUpdate() and any airfeilds not in Airfeilds6.txt will be removed from list of filenames

Step 2) Start TODC and wait for first calc to finish.
Step 3) In 'save' pop up, go to correct folder for saving files.
Step 4) Move 'save' pop up to top RHC of screen.
Step 5) Ensure non white background under save pop up
Step 6) Run startCalc() to activtae clicker

files required in folder:
autoSaver.py
runways6.txt #list of filenames (required)
Airfeilds6.txt #list of airfeilds to exclude (optional)

'''
import os
import pyautogui as p
import time
from datetime import datetime
import tkinter as tk
from tkinter import filedialog

#initialise runway the variable that will store filenames. Needs to be accessible to all functions.
#global runway
runway = []


#this function updates the file runways6.txt with a list of all the runway intersections available in TODC from the latest nav blue AODB file (which TODC is also using)
def runways6Update(): 
    AODBs = []#variable for AODB files
    date = []#variable for dates in AODB filenames
    global runway

    for file in os.listdir("C:/NAVBLUE/ToDc Office ASL Airlines Ireland A300-622"): #standard location of AODB that TODC uses. Update folder as required.
        if file.startswith("AIRCON.AIRBUS_A300-622"):
            #print(os.path.join("C:/NAVBLUE/ToDc Office ASL Airlines Ireland A300-622/", file))#for testing
            AODBs.append(file)  #make list of all AODBs in folder

    #find latest AODB
    for AODB in AODBs:
        info = AODB.split('_')
        date.append(info[1][9:]+'.'+info[2].strip('.TXT'))
    file = AODBs[date.index(max(date))]

    #open and read latest AODB and get all runway intersections
    f = open("C:/NAVBLUE/ToDc Office ASL Airlines Ireland A300-622/"+file, 'rt')
    x = f.readlines()			#each line of text file becomes item in list x
    f.close()

    #x = x[0:100]#for testing
    for n, i in enumerate(x):	#cycle through each line of text (items in list x)
        b = i.split(' ')        #b is now a list of all the words in line i
        if len(b) > 1:          #make sure there is more than one word on line
            if b[1] == '150':   #if second word is '150' this means it's an airfeild name line, and the airfeild name will be the next word (this is NavBlue A300 AODB convention)
                airfeild = b[2]
            if b[1] == '200':   #if second word is '200' this is a runway intersection line, and next word will be runway intersection name
                runway.append(airfeild.strip('"')+' '+b[2].strip('"')) #strip extra quotation marks from string, and add Airfeild+runwayIntersection to list of runways

    runway.sort()           #put it in same order as TODC runs calculations (this is different from the order of the AODB)

    #write runway intersections to file runway6.txt (also saved in runway varieble). file is so manual adjutments can be made to list easily
    runwayfile = open('runways6.txt', 'w')
    for item in runway:
     runwayfile.write(item+'\n')

    runwayfile.close()
    print('runways6Update() complete')

#create runway filenames from runways6.txt (not nessissary if you just ran runway6Update, but nessissary if you made any manual ajustments to runways6.txt file)
def runwayUpdate():
    global runway
    runwayList = 'runways6.txt'
    f = open(runwayList, 'rt')
    runway = f.readlines()			#each line of text file becomes item in list x
    f.close()

    for i in runway:
        runway[runway.index(i)] = i.strip('\n') #removes newline char form file. format of runway file names is 'ABCD 01CJTMP' 
    print('runwayUpdate() complete')

#remove airfields not in file Airfeild6.txt from runway (can't really run whole AODB as TODC gets very slow, likely only will need to run some airfeilds)
def airfeildsUpdate():
    global runway
    AirfeildList = 'Airfeild6.txt'
    f = open(AirfeildList, 'rt')
    Airfeild = f.readlines()			#each line of text file becomes item in list x
    f.close()

    for j in Airfeild:
        Airfeild[Airfeild.index(j)] = j.strip('\n')

    removed = []

    for l, k in enumerate(runway):  #don't remove stuff from list as you are cycling through it, this messes up the cycling process
        check = False               #cehck every runway intersection if the airfeild is in airfeilds6.txt. If it isn't, remove runway intersection from runway
        for a in Airfeild:
            if k[:4] == a:
                check = True
        if check == False:
            removed.append(k)

    for m in removed:
        runway.remove(m)
    print('airfeildsUpdate() compelete')


#start job that clicks on save button when this appears on screen. Saves file according to the contects of runway (as updated in prev functions)
def startCalc ():
    global runway
    width, height = p.size() #returns screen dimesnisions in pixels (for moouse movements)
    save = ((width*1972/2256),(height*997/1504)) #if you set 'save' pop up to appear in top RHC
    startTime = datetime.now()
    print('Calc start: ')
    print(startTime)

    #runway1 = [('EBBR 25RB3TMP'),('EBBR 25RB5')] (for testing)


    for n, runwayIntersection in enumerate(runway):
        timeElapsed = (datetime.now()-startTime).total_seconds()
        startTime = datetime.now()
        print('Calc time: '+str(round(timeElapsed/60,2))+'min')
        print(runwayIntersection)
        im = p.screenshot()
        while im.getpixel(save) != (225, 225, 225):         #takes a screenshot every 15secs and checks the colour is the save pixel. when it's white, save pop up is there
            im = p.screenshot()
            time.sleep(15)
        #this code is executed when save pop up appears (save pixel is white)
        p.write(runwayIntersection) #writes the file name (when save pop up appears, text feild is automatically highlighted)
        time.sleep(2)
        p.press('enter')
        time.sleep(4)
        #p.click(save)
        #p.moveTo(1900, 900) #move mouse out of the way because now it's on the save pixel (which we need to be able to see the colour of)

#prepares filenames of all runway intersections in chosen airfeilds from AODB and starts waiting to click save
def runAll():
    runways6Update()
    airfeildsUpdate()
    startCalc()

#main
#prints functions available and GUI to run functions
    
h = ('''
functions available:
runways6Update()    update runways6.txt with latest runway intersections from latest AODB
runwayUpdate()      create runway filenames from runways6.txt
airfeildsUpdate():  Only do runway intersections in Airfeilds6.txt (remove runways not from airfeilds on list Airfeilds6)
startCalc ():       start looking for save box to save and click. only do this once filenames (runway) match what's lined up in TODC
to see runway list: runway
type h to see this list again
     ''')
print(h)


root= tk.Tk()

canvas1 = tk.Canvas(root, width = 900, height = 600, bg = 'lightsteelblue')
canvas1.pack()
    
    
browseButton_Excel = tk.Button(text='Import AODB', command=runways6Update, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(450, 100, window=browseButton_Excel)

browseButton_Excel = tk.Button(text='import Runways6', command=runwayUpdate, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(450, 200, window=browseButton_Excel)

browseButton_Excel = tk.Button(text='Remove Airfeilds', command=airfeildsUpdate, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(450, 300, window=browseButton_Excel)

browseButton_Excel = tk.Button(text='Start save-clicker for TODC', command=startCalc, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(450, 400, window=browseButton_Excel)

browseButton_Excel = tk.Button(text='Run All', command=runAll, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(450, 500, window=browseButton_Excel)


root.mainloop()






