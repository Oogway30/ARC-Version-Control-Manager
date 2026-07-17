import os
import shutil
import hashlib


def calculate_file_hash(file_path):
    with open(file_path, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    return file_hash

def add(args:dict=None):
    
    if args.path[0] == "./": 
        filesPaths = "./"
    
    elif args.path[0]=='./' and len(args.path)>1:
        raise IndexError
    else:
        filesPaths = args.path 
   

    if "ARC" not in os.listdir(): 
        return "Initialize First!"


    if filesPaths=="./":
        filesToCopy = os.listdir(filesPaths)
        filesToCopy.remove("ARC")
        for file in filesToCopy:
            if file.startswith(".") or file.startswith("_"):
                continue
            try:
                if os.path.isdir(f"./{file}"):
                    if file in os.listdir("./ARC/temporary"):
                        shutil.rmtree(f"./ARC/temporary/{file}")
                    shutil.copytree(f"./{file}",f"./ARC/temporary/{file}")
                    print(f"added: {file}")
                else:
                    try:
                        fileHash = calculate_file_hash(f"./{file}")
                        if file in os.listdir("./ARC/temporary") and fileHash == calculate_file_hash(f"./ARC/temporary/{file}"):
                            continue   
                        elif file in os.listdir("./ARC/temporary") and fileHash != calculate_file_hash(f"./ARC/tmemporary/{file}"):
                            os.remove(f"./ARC/temporary/{file}")
                        raise WindowsError
                    except:
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
                print(f"File/Folder does not exist: {filePath}")

    return "File(s)/ Folder(s) added Successfully!"


def untracked_files(args):
    args = None
    untrackedFiles = []
    filesInDIR = os.listdir("./")
    if "ARC" not in os.listdir("./"): 
        return "Initialize First!"
    filesInDIR.remove("ARC")
    for filePath in filesInDIR:
        if filePath.startswith(".") or filePath.startswith("_"):
            continue
        if os.path.isdir(f"./{filePath}"):
            continue
        fileHash = calculate_file_hash(f"./{filePath}")
        if filePath in os.listdir("./ARC/temporary") and fileHash == calculate_file_hash(f"./ARC/temporary/{filePath}"):
            continue   
        elif filePath in os.listdir("./ARC/temporary") and fileHash != calculate_file_hash(f"./ARC/tmemporary/{filePath}"):
            untrackedFiles.append(filePath)
        elif filePath not in os.listdir("./ARC/temporary"):
            untrackedFiles.append(filePath)
    for file in untrackedFiles:
        print(file)

