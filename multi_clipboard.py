import sys
import clipboard 
import json 

SAVED_DATA = "clipboard.json"

def save_data(filepath,data):
    with open(filepath,"w") as f:
        json.dump(data,f)

def load_data(filepath):
    with open(filepath,"r") as f:
        data = json.load(f)
        return data




if len(sys.argv)==2:
    command = sys.argv[1]
    print(command)
    data = load_data(SAVED_DATA)

    if command=="save":
        key = input("ENTER A KEY: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA,data)
    elif command=="load":
        pass
    elif command=="list":
        pass
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command. ")
