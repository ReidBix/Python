__author__ = 'Reid'

import os, json

def main():
    with open('file_info.txt') as data_file:
        l = json.load(data_file)
    txt = l[0]
    d = l[1]
    for x in d:
        x = str(x)
        file_path = txt + "/" +  x
        with open(file_path) as f:
            for i, l in enumerate(f):
                pass
            i += 1
        if (d[x] != i):
            pString = "The number of lines found in file " + str(x) + " was " + str(i) + " but was expected to be " + str(d[x])
            print(pString)
    return 0

if __name__ == "__main__":
    main()
