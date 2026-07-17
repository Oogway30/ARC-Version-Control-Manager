import os
from temporary import calculate_file_hash
import datetime
import shutil
def commit(args:dict=None):
#def commit():
    message = args.message
    Metadata = {"author":None,"timestamp":datetime.datetime.now(),"message":message,"files":{}}
    if "ARC" not in os.listdir('./'): 
        return "Initialize First!"

    filesToAdd = os.listdir("./ARC/temporary")
    repositories = os.listdir("./ARC/repositories")
    lenghtOfRepo = len(os.listdir("./ARC/repositories"))
    if filesToAdd and not(repositories):
        os.mkdir(f"./ARC/repositories/{lenghtOfRepo}")
        for file in filesToAdd:
            if os.path.isdir(f"./ARC/temporary/{file}"):
                continue
            
            PathToFile = f"./ARC/temporary/{file}"
            
            Metadata["files"][PathToFile] = calculate_file_hash(file)
            newFileName = f"{Metadata["files"][PathToFile]}{os.path.splitext(file)[1]}"
            os.rename(PathToFile,f"./ARC/temporary/{newFileName}")
            shutil.copyfile(f"./ARC/temporary/{newFileName}",f"./ARC/repositories/{lenghtOfRepo}/{newFileName}")
            os.remove(f"./ARC/temporary/{newFileName}")
            print(f"removed: {file} with the hash: {newFileName}")
        
        return Metadata
