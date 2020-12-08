#!/usr/bin/python3

# Select the info to get off of the file
returnItems = ["Name", "Version", "About", "Developer", "Website", "Binary"]

# Set the package to install
packageName = "package-example"

# Import modules that are needed
import json, requests

# Prepare "repo.list"
file = "../repo.list"

# Open the file
f = open(file, "r")
repos = f.read().split()

# Download data
for url in repos:
    packageFile = url + packageName + "/manifest.json"
    r = requests.get(packageFile, allow_redirects=True)
    
    open("manifest.json", 'wb').write(r.content)
    
    if str(r) == "<Response [404]>":
        print(url +  " is an invalid repository or package.")

# Open the json file
jsonFile = open("manifest.json", "r")

# Read the file
f = json.load(jsonFile)

# Return Values
for returnItem in returnItems:
	print(returnItem + ": " + f[returnItem]) 

jsonFile.close()