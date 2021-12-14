import os

# Fetching Directory Path from user
path = input("Enter Directory Path To Open Http Server: \n")
localhostport = input("Desired Port (If Any): \n")

# Changing current working directory
os.chdir(path)

# Running Server command in changed Directory
if localhostport == "":
    os.system("python -m http.server")
else:
    os.system(f"python -m http.server {localhostport}")