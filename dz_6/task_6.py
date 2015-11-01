#coding: utf-8

def find(rash,path): #6.1 
    import os
    names = os.listdir(path)

    for name in names:
        if name.endswith(rash):
            for i,line in enumerate(open(path + "/"+ name)):
                yield name,i,line
            
def grep(gen,substr): #6.2

    for name,i,line in gen:
        if substr in line:
            yield name,i,line

for name,i,line in grep(find('.txt','.'),'р'): #6.3
    print(name,i,line)

import argparse #6.4 в коммандной строке: python task_6.py .txt . р

parser = argparse.ArgumentParser(description='Enter path, rash, substr.')
parser.add_argument('rash')
parser.add_argument('path')
parser.add_argument('substr')
args = parser.parse_args()

for name,i,line in grep(find(args.rash,args.path),args.substr):
    print(name,i,line)



