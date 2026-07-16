import os
def init(args):
    args = None

    if "ARC" not in os.listdir(): 
        os.mkdir("./ARC")
        os.mkdir("./ARC/repos")
        os.mkdir("./ARC/temporary")
        return "Successfully Initialized!"
    else:
        return "Already initialised!"