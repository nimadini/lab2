import os
import sys

root_dir = 'HelloWorld/src'
for root, subFolders, files in os.walk(root_dir):
    for f in files:
        ''' uncomment if you want to change root_dir to '.'
        if f == 'count.py':
            continue '''
        myFile = open(os.path.join(root, f), 'r')
        for line in myFile:
            if len(line.strip()) > 80:
                print 'log (inside python code): ' + line.strip()
                sys.exit(1)
sys.exit(0)