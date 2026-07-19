import os as os
import json
from temporary import calculate_file_hash
from datetime import datetime as dt

import shutil
def get_Commit_Metadata(CommitNr):
    if os.listdir("./ARC/repositories")[-1] >= CommitNr:
        with open(f"./ARC/repositories/{CommitNr}/Metadata_{CommitNr}.json","w") as MetadataFile:
            Metadata = json.load(MetadataFile)
        return Metadata
    else:
        return f"No CommitNr: {CommitNr}"
    
def get_last_Commit_Metadata():
    lastCommitNRInFunc = os.listdir("./ARC/repositories")[-1]
    with open(f"./ARC/repositories/{lastCommitNRInFunc}/Metadata_{lastCommitNRInFunc}.json","r") as MetadataFile:
        Metadata = json.load(MetadataFile)
    return Metadata

def helperFunction(FileHash,PathToFile, lenghtOfRepo, Metadata, file):
    os.rename(PathToFile,f"./ARC/temporary/{FileHash}{os.path.splitext(file)[1]}")
    shutil.move(f"./ARC/temporary/{FileHash}{os.path.splitext(file)[1]}",f"./ARC/.objects/{FileHash}{os.path.splitext(file)[1]}")
    #shutil.copyfile(f"./ARC/temporary/{FileHash}",f"./ARC/.objects/{FileHash}")
    #os.remove(f"./ARC/temporary/{FileHash}")
    print(f"removed: {file} with the hash: {FileHash}")

    Metadata["timestamp"] = str(dt.now().isoformat())
    with open(f"./ARC/repositories/{lenghtOfRepo}/Metadata_{lenghtOfRepo}.json","w") as MetadataFile:
        json.dump(Metadata,MetadataFile)
                        

def commit(args:dict=None):

    if "ARC" not in os.listdir('./'): 
        return "Initialize First!"
    if not os.listdir('./ARC/temporary'): 
        return "Nothing to Commit!"
    
    with open("./ARC/.generalMetadataARC.json","r") as generalMetadata:
            authorFromFile = json.load(generalMetadata)["author"]

    message = "args.message"
    Metadata = {"author":authorFromFile,"timestamp":None,"message":message,"files":{},"changedFiles":{},"newlyAddedFiles":{}}
    filesToAdd = os.listdir("./ARC/temporary")
    repositories = os.listdir("./ARC/repositories")
    lenghtOfRepo = len(repositories)+1

    if filesToAdd and lenghtOfRepo ==1 :
        try:
            os.mkdir(f"./ARC/repositories/{lenghtOfRepo}")
            for file in filesToAdd:
                if os.path.isdir(f"./ARC/temporary/{file}"):
                    continue
                FileHash = calculate_file_hash(f"./ARC/temporary/{file}")
                PathToFile = f"./ARC/temporary/{file}"
                Metadata["files"][file] = f"{FileHash}{os.path.splitext(file)[1]}"
                helperFunction(FileHash,PathToFile, lenghtOfRepo, Metadata, file)
            return {"status":"Success"}

        except Exception as err:
            return {"status":"Failure","Exception":err}
    else:
        try:
            lastCommitPath = f"./ARC/repositories/{os.listdir("./ARC/repositories/")[-1]}"
            lastCommitNR = int(os.listdir("./ARC/repositories/")[-1])
            lastCommitMetadata = get_last_Commit_Metadata()["files"]
            os.mkdir(f"./ARC/repositories/{lastCommitNR+1}")
            for file in lastCommitMetadata:
                Metadata["files"][file] = lastCommitMetadata[file]
            for file in filesToAdd:
                PathToFile = f"./ARC/temporary/{file}"
                if os.path.isdir(f"./ARC/temporary/{file}"):
                    continue
                PathToFile = f"./ARC/temporary/{file}"
                FileHash = calculate_file_hash(file)
                try:
                    if Metadata["files"][file] and Metadata["files"][file] == FileHash:
                        Metadata["files"][file] = lastCommitMetadata[file] #changed the names from lastcommitmetadata to metadata as lastcommitmetadata (file info) has been saved to metadata file and chnaged only if the hash has been changed

                        os.remove(f"./ARC/temporary/{file}")
                        Metadata["timestamp"] = str(dt.now().isoformat())
                        with open(f"./ARC/repositories/{lenghtOfRepo}/Metadata_{lenghtOfRepo}.json","w") as MetadataFile:
                            json.dump(Metadata,MetadataFile)
                            
                        
                    
                    elif Metadata["files"][file] and Metadata["files"][file] != FileHash:
                        Metadata["files"][file] = f"{FileHash}{os.path.splitext(file)[1]}"
                        Metadata["changedFiles"][file] = f"{FileHash}{os.path.splitext(file)[1]}" 
                        helperFunction(FileHash,PathToFile, lenghtOfRepo, Metadata, file)   
                except KeyError:                    
                    
                    Metadata["files"][file] = f"{FileHash}{[os.path.splitext(file)[1]]}"
                    Metadata["newlyAddedFiles"][file] = f"{FileHash}{os.path.splitext(file)[1]}" 
                    helperFunction(FileHash,PathToFile, lenghtOfRepo, Metadata, file)
            return {"status":"Success"}
        except Exception as err:
            return {"status":"Failure","Exception":err}
        
def checkout(CommitNR):
    try:
        filesToAdd = get_Commit_Metadata(CommitNR)['files']
    except:
        return filesToAdd
    
    filesToReplace = os.listdir("./")
    for file in filesToReplace:
        if file.startswith('.') or file.startswith("_") or os.path.isdir(file):
            continue
        os.remove(file)
    for fileToAdd in filesToAdd:
        shutil.move(f"./ARC/temporary/{fileToAdd}")
    
#Something changed here!!