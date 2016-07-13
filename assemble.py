from sh import jpegtran, montage
from pprint import pprint
from os import listdir




i=sorted(listdir('i'))
d=sorted(listdir('d'))

assert len(i) == len(d)

for n in range(len(i)):
    I="i/trans_%s" % i[n]
    D="d/trans_%s" % d[n]
    jpegtran("-transverse", "i/%s" % i[n], _out=I)
    jpegtran("-transverse", "d/%s" % d[n], _out=D)

    montage('-tile', '2x1',
            '-geometry','+0+0',
            I, D, "stereo/%s_%s.jpg" % (i[n].replace('.JPG',''),d[n].replace('.JPG','')))
            

