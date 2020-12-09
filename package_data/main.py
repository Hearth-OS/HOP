#!/usr/bin/python3

# Import modules that are needed
import json, requests, sys, os

# Select the info to get off of the file
returnItems = ["Name", "Version", "About", "Developer", "Website"]

# Set the package to install
packageName = str(sys.argv[1])


# Prepare "repo.list"
file = "../repo.list"

# Open the file
f = open(file, "r")
repos = f.read().split()
aRepoFound = False

# Download data
for url in repos:
    packageFile = url + packageName + "/manifest.json"
    binary = url + packageName + "/install"
    r = requests.get(packageFile, allow_redirects=True)
    
    open("manifest.json", 'wb').write(r.content)
    
    # Pass if no package is found.
    if str(r) == "<Response [404]>" and aRepoFound == False:
        pass
        
    if str(r) == "<Response [200]>" and aRepoFound == False:
        aRepoFound = True
        # Open the json file
        jsonFile = open("manifest.json", "r")
        
        # Read the file
        f = json.load(jsonFile)
        
        # Return Values
        for returnItem in returnItems:
            print(returnItem + ": " + f[returnItem]) 
        
        jsonFile.close()
        
        # Add an extra line to make it easy to read
        print()
        
        # Ask if the user wishes to install it and do so if they do.
        while True:
            yn = input("Would you like to install it? (y/n) ")
            
            if yn.lower() == "y":
                break
            
            if yn.lower() == "n":
                break
            
            else:
                print()
        
        # Download & Install the package
        if yn.lower() == "y":
            print("Downloading " + binary)
            r = requests.get(binary, allow_redirects=True)
            open("install", 'wb').write(r.content)
            os.system("chmod +x ./install && ./install")
            
        
# If no package is found state that to the user
if aRepoFound == False:
    print("Package not found")
