import os

print("[Warn] HOP for Chrome OS is in beta!")
# Make folders
os.system("mkdir /apps")
os.system("mkdir /apps/hop_files")

# Copy HOP files
os.system("cp ../repo.list /apps/hop_files")
os.system("sudo cp ../package_data/main.py /usr/local/bin/hop")
os.system("sudo chmod +x /usr/local/bin/hop")

# Install modules
os.system("python3 -m pip install rich")
os.system("python3 -m pip install requests")
os.system("python3 -m pip install json")
