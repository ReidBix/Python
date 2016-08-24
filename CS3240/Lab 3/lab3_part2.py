__author__ = 'Reid'

import os, json

def main():
    d = {}
    dir = os.getcwd() #current working directory
    listDir = os.listdir(dir) #list of names in directory
    for x in listDir:
        if not (os.path.isdir(x)):
            with open(x) as f:
                for i, l in enumerate(f):
                    pass
            i += 1
            d.update({x:i})
    l = []
    l.append(dir)
    l.append(d)
    with open('file_info.txt','w') as outfile:
        json.dump(l,outfile)

if __name__ == "__main__":
    main()
