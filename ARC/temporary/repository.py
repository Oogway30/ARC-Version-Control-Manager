import os
def init(args):
    args = None

    if "ARC" not in os.listdir(): 
        os.mkdir("./ARC")
        os.mkdir("./ARC/repositories")
        os.mkdir("./ARC/temporary")
        print("Successfully Initialized!")
    else:
        print("Already initialised!")