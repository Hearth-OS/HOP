#!/usr/local/bin/python3

help = '''
HOP
Hearth OS Package manager
Version 1.0

Install a package: hop install <package_name>
Check for an update of a package: hop update 
'''

# Import modules that are needed
import json, requests, sys, os, rich

from rich.console import Console
from rich.prompt import Confirm
from rich.panel import Panel

console = Console()
console.print()

os.system("cd /tmp")

# Select the info to get off of the file
returnItems = ["Name", "Version", "About", "Developer", "Website", "AppID"]

# Set the package to install
try:
    function = str(sys.argv[1])
    
    if function == "install":
        packageName = str(sys.argv[2])
    elif function == "update":
        packageName = str(sys.argv[2])
    
    else:
        rich.print(help)
except:
    rich.print(help)
    
    sys.exit()
    

# Prepare "repo.list"
file = "/apps/hop_files/repo.list"

# Open the file
f = open(file, "r")
repos = f.read().split()
aRepoFound = False

# Download data
if function == "install":
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
                rich.print(returnItem + ": " + f[returnItem])
                
                if returnItem == "AppID":
                    appid = str(f[returnItem])
                if returnItem == "Version":
                    version = str(f[returnItem])
            
            jsonFile.close()
        
            # Add an extra line to make it easy to read
            print()
        
            # Ask if the user wishes to install it and do so if they do.
            while True:
                console.print("Never installing packages from untrusted developers!", style="blink bold red")
                yn = Confirm.ask("Would you like to install it?")
                
                if yn == True:
                    break
                
                if yn == False:
                    break
                
                else:
                    print()
            
            # Download & Install the package
            if yn == True:
                print()
                with console.status("[bold green]Installing...") as status:                
                    r = requests.get(binary, allow_redirects=True)
                    open("installHOP", 'wb').write(r.content)
                    
                    os.system("mkdir /apps/" + str(appid) + " && chmod +x ./installHOP && ./installHOP")
                    try:
                        rich.print("[green] :white_check_mark: Installed")
                    except:
                        rich.print("[red] :x: Install failed")
                
            
    # If no package is found state that to the user
    if aRepoFound == False:
        console.print("No package found", style="blink bold red")


# Update a package
if function == "update":
    for url in repos:
        packageFile = url + packageName + "/manifest.json"
        binary = url + packageName + "/installHOP.sh"
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
                if returnItem == "Name":
                    name = f[returnItem]
                if returnItem == "Version": 
                    rich.print("Current version is " + f[returnItem])
                    
                    try:
                        version = float(f[returnItem])
                        
                        appFile = "/apps/"
                        if version > 1:
                            print("detection")
                    except:
                        console.print("Error on repository configuration.", style="blink bold red")
            
            jsonFile.close()
        
            # Add an extra line to make it easy to read
            print()
