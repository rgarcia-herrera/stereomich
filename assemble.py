from sh import jpegtran, montage, convert
from pprint import pprint
from os import listdir, unlink




i=sorted(listdir('i'))
d=sorted(listdir('d'))

assert len(i) == len(d)

trash = []

for n in range(len(i)):
    I="tmp/i/trans_%s" % i[n]
    D="tmp/d/trans_%s" % d[n]

    # transverse op flops the photos
    jpegtran("-transverse", "i/%s" % i[n], _out=I)
    jpegtran("-transverse", "d/%s" % d[n], _out=D)
    trash += [I, D]

    montage_flopped = "stereo/flopped_%s_%s.jpg" \
                      % (i[n].replace('.JPG',''),
                         d[n].replace('.JPG',''))
    montage('-tile', '2x1',
            '-geometry','+0+0',
            I, D,
            montage_flopped)

    montage_unflopped = "stereo/%s_%s.jpg" \
                        % (i[n].replace('.JPG',''),
                           d[n].replace('.JPG',''))
    convert(montage_flopped,
            '-flop',
            montage_unflopped)

    trash.append(montage_flopped)
    


for f in trash:
    unlink(f)
    
