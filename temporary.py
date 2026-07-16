import os
import shutil
import hashlib

def add(args:dict=None):

    filesPaths = args.path
    #print(f"Current folder layout: {filesToCopy}")
    
    if "ARC" not in os.listdir(): 
        return "Initialize First!"


    if filesPaths=="./":
        filesToCopy = os.listdir(filesPaths)
        filesToCopy.remove("ARC")
        for file in filesToCopy:
            try:
                if os.path.isdir(f"./{file}"):
                    shutil.copytree(f"./{file}",f"./ARC/temporary/{file}")
                    print(f"added: {file}")
                else:
                    shutil.copy(f"./{file}","./ARC/temporary")
                    print(f"added: {file}")
            except Exception as e:
                print(f"Skipped: {file}")
                print(e)
    
    else:
        for filePath in filesPaths:
            if os.path.exists(filePath):
                try:
                    if os.path.isdir(f"./{filePath}"):
                        shutil.copytree(f"./{filePath}",f"./ARC/temporary/{filePath}")
                        print(f"added: {filePath}")
                    else:
                        shutil.copy(f"./{filePath}","./ARC/temporary")
                        print(f"added: {filePath}")
                except Exception as e:
                    print(f"Skipped: {filePath}")
                    print(e)
            else:
                print(f"File/Folder does not exist: {filesPaths}")


    #print(f"Current temporary folder layout: {os.listdir(f"{filesPaths}ARC/temporary")}")

