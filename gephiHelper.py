import json
import pandas as pd
import argparse
from pathlib import Path


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    return parser.parse_args()

def findFile(path):
    start = len(path)
    for i in range(len(path) - 1, -1, -1):
        if path[i] == '/':
            start = i + 1
            break
    return path[start:]

def convertToCSV(filePath):
    with open(filePath) as file:
        data = json.load(file)
    cee = []
    cer = []

    for entry in data["Calls"]:
        callee = entry["Callee"]
        new_callee = []
        new_callee.append(findFile(callee[1]))
        new_callee.append(callee[2])
        new_callee.append(callee[3])
        cee.append(new_callee)

        caller = entry["Caller"]
        new_caller = []
        new_caller.append(findFile(caller[1]))
        new_caller.append(caller[2])
        new_caller.append(caller[3])
        cer.append(new_caller)

    dict = {'callee': cee, 'caller': cer}
    df = pd.DataFrame(dict)
    df.to_csv('toGarph.csv')

if __name__ == '__main__':
    args = _parse_args()
    if args.filepath is None:
        print("Target file does not exist or is not specified")
        raise SystemExit(1)
    target = Path(args.filepath)
    convertToCSV(target)
<<<<<<< HEAD


=======
>>>>>>> 0c74790fd549f16b8677e014f6773676d7d89192
