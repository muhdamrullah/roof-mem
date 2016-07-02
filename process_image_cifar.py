from PIL import Image
import numpy as np
import sys
import os
from scipy import ndimage
import cPickle as pickle
import gzip

if len(sys.argv) < 2:
    print "Usage: python process_single.py input_folder"
    exit(1)

# input folder
fi = sys.argv[1]

# init var
classes = os.listdir(fi)
set_x = []
set_y = []
k = 0 # idx for classes
list_classes = []
new_im = []

# Create sets
for cls in classes:
        list_classes.append(cls)
        imgs = os.listdir(fi + cls)
        for img in imgs:
                im = Image.open(fi + cls + '/' + img)
                im = (np.array(im))
                r = im[:,:,0].flatten()
                g = im[:,:,1].flatten()
                b = im[:,:,2].flatten()
                new_im.append(list(r) + list(g) + list(b))
                print new_im
                set_x.append(new_im)
                set_y.append(k)
        k +=1

set_x = np.array(new_im, np.uint8)
print set_x.shape
print set_x
image_dictionary = {}
image_dictionary['data'] = set_x
image_dictionary['label'] = set_y

with open('data.pkl', 'wb') as f:
    pickle.dump(image_dictionary, f, -1)
f.close()
