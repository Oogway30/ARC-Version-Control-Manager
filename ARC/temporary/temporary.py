import os
import shutil
import hashlib


def calculate_file_hash(file_path):
    with open(file_path, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    return file_hash

def add(args:dict=None):
    countAddedFiles = 0
    AddedFiles = []
    SkippedFiles = []
    ErrorMessage = []
    UnchangedFiles = []

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
                    AddedFiles.append(file)
                else:
                    try:
                        fileHash = calculate_file_hash(f"./{file}")
                        if file in os.listdir("./ARC/temporary") and fileHash == calculate_file_hash(f"./ARC/temporary/{file}"):
                            UnchangedFiles.append(file)   
                            continue
                        elif file in os.listdir("./ARC/temporary") and fileHash != calculate_file_hash(f"./ARC/temporary/{file}"):
                            os.remove(f"./ARC/temporary/{file}")
                        raise WindowsError
                    except:
                        shutil.copy(f"./{file}","./ARC/temporary")
                        AddedFiles.append(file)
                    
            except Exception as e:
                SkippedFiles.append(file)
                ErrorMessage.append(e)
            
            
    
    else:
        for filePath in filesPaths:
            if os.path.exists(filePath):
                
                fileName = os.path.basename(filePath).split('/')[-1]
                if fileName.startswith(".") or fileName.startswith("_"):
                    SkippedFiles.append(fileName)
                    continue
                try:
                    if os.path.isdir(filePath):
                        if fileName in os.listdir("./ARC/temporary"):
                            shutil.rmtree(f"./ARC/temporary/{fileName}")
                        shutil.copytree(filePath,f"./ARC/temporary/{fileName}")
                        AddedFiles.append(fileName)
                    else:
                        try:
                            fileHash = calculate_file_hash(filePath)
                            if fileName in os.listdir("./ARC/temporary") and fileHash == calculate_file_hash(f"./ARC/temporary/{fileName}"):
                                UnchangedFiles.append(fileName)   
                                continue
                            elif fileName in os.listdir("./ARC/temporary") and fileHash != calculate_file_hash(f"./ARC/temporary/{fileName}"):
                                os.remove(f"./ARC/temporary/{fileName}")
                            raise WindowsError
                           
                        except:
                            shutil.copy(filePath,"./ARC/temporary")
                            AddedFiles.append(fileName)
                except Exception as e:
                    SkippedFiles.append(fileName)
                    ErrorMessage.append(e)
            else:
                print(f"File/Folder does not exist: {filePath}")

    print("Added Files:")
    for file in AddedFiles:
        print(f"\t{file}")

    print("\n")

    print("Skipped Files:")
    for file in SkippedFiles:
        print(f"\t{file}")

    print("\n")

    print("Unchanged Files:")
    for unchangedFile in UnchangedFiles:
        print(f"\t{unchangedFile}")

    print("\n")

    print("Error Messages:")
    for err in ErrorMessage:
        print(f"\t{err}")

    print("\n")

    return f"{len(AddedFiles)} File(s)/ Folder(s) added Successfully!"


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
        elif filePath in os.listdir("./ARC/temporary") and fileHash != calculate_file_hash(f"./ARC/temporary/{filePath}"):
            untrackedFiles.append(filePath)
        elif filePath not in os.listdir("./ARC/temporary"):
            untrackedFiles.append(filePath)
    print("Untracked Files:")
    for file in untrackedFiles:
        print(f"\t{file}")
    print("\n")
    print(f"{len(untrackedFiles)} File(s)/ Folder(s) untracked.")

