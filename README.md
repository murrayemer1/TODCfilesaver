# TODCfilesaver
saves files as they are created by the aircraft performance software 'TODC'

This program's main purpose is to save calcs run by TODC and name them as per list of names (in variable 'runway')

There are also some functions to choose what file names appear in runway (the contents of runway must match the TODC calculations):
1. You can update 'runway' with names listed in the file 'runways6.txt' using runwayUpdate() or clicking 'import Runways6'. (manually type names into Runways6, click import Runways6 and then click 'Start save-clicker for TODC Calculation')
2. You can remove any airfeilds not listed in in Airfeilds6.txt from runway using airfeildsUpdae() or clicking 'remove all airfeilds execpt those in Airfeilds6'
4. runways6.txt can be updated with all runways intersections in the latest TODC AODB using runways6Update


### Limitations:
This program __DOES NOT__ look for the 'save' pop up, or change the folder where files get saved. It will only save if pop up is in correct location (top RHC of pop up is in top RHC of screen) and there is a non white background under the pop up
This program does ajust for screen size


### How to use this program:
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
  * autoSaver.py
  * runways6.txt (list of filenames -required)
  * Airfeilds6.txt (list of airfeilds to include -optional)
