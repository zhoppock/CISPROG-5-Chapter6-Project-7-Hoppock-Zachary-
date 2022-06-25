import os

def displayFiles(pathname):
  if os.path.isfile(pathname):
    name = os.path.basename(pathname)
    openFile = open(pathname,"r")
    fileContents = openFile.readlines()
    print("\n" + name + ":")
    for eachContent in fileContents:
        print(eachContent)
  elif os.path.isdir(pathname):
    GetDirectories = os.listdir(pathname)
    for eachItem in GetDirectories:
      completePath = os.path.join(pathname,eachItem)
      print("File name: ",completePath)
      isdirectory = os.path.isdir(completePath)
      if isdirectory or os.path.isfile(completePath):
        displayFiles(completePath)

def main():
  pathname = input("Enter File name/directory path or press ENTER to quit: ")
  while True:
    if pathname == "":
      break
    elif os.path.isfile(pathname) or os.path.isdir(pathname):
      displayFiles(pathname)
      pathname = input("\nEnter File name/directory path or press ENTER to quit: ")
    else:
      print("Invalid path name.")
      pathname = input("\nEnter File name/directory path or press ENTER to quit: ")