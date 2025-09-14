import getopt 
import os
import sys

def main(argv):
    opts , args = getopt.getopt(argv,'i:')
    for o , a in opts:
        if o == '-i':
            run(a)

def run(a):
    cpp_file = a+'.cpp'
    exe_file = a+'.exe'
    os.system('g++'+cpp_file+'-o'+exe_file)
    os.system(exe_file)
    
if __name__=="__main__":
    main(sys.argv[1])

