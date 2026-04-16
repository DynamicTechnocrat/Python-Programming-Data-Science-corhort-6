import os

location = "C:/Users/OWNER/Desktop/mrsade" ## file location

files_in_original = os.listdir(location) ### list of file in that folder


for file in files_in_original: ### loop through the list of file 
    print(file) ## print the name of the file one after the other
    print(type(file)) ## print the type of the file name (string)
    print(location + "/" +  file) ## print the location of the file with the name of the file which is the address of the file

destination = "C:/Users/OWNER/Desktop/mrjames" ### destination location

### loop through the list of file and move the file to the destination location

import shutil ### 

for file in files_in_original: ### loop through the list of file
    shutil.move(location + "/" + file , destination + "/" + file) ### move the file to the destination location


