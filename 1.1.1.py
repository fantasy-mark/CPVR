from PIL import Image
import os

filelist = ["test2.png"]

for infile in filelist:
    outfile = os.path.splitext(infile)[0] + '.jpg'
    print "outfile : ", outfile
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print "can't convert", infile