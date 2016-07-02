import os
import sys
import h5py
from scipy import ndimage
import numpy as np
import pickle

if len(sys.argv) < 2:
    print "Usage: python gen_h5.py input_folder"
    exit(1)

# input folder
fi = sys.argv[1]

# init var
classes = os.listdir(fi)
set_x = []
set_y = []
k = 0 # idx for classes
list_classes = []

# Create sets
for cls in classes:
	list_classes.append(cls)
	imgs = os.listdir(fi + cls)
	for img in imgs:
		im = ndimage.imread(fi + cls + '/' + img)
		# Create sets
for cls in classes:
        list_classes.append(cls)
        imgs = os.listdir(fi + cls)
        for img in imgs:
                im = ndimage.imread(fi + cls + '/' + img)
                r = im[:,:,0].flatten()
                g = im[:,:,1].flatten()
                b = im[:,:,2].flatten()
                new_im = np.array(list(r) + list(g) + list(b), np.uint8)
#               print im.shape
                set_x.append(im)
                set_y.append(k)
        k +=1

# sets to numpy arrays
set_x = np.array(set_x)
set_y = np.array(set_y)

# shuffle sets
rp = np.random.permutation(set_x.shape[0])
set_x = set_x[rp,:]
set_y = set_y[rp]

# divide sets, train or valid
valid_set_x = set_x[0:set_x.shape[0]/10,:]
valid_set_y = set_y[0:set_x.shape[0]/10]
train_set_x = set_x[set_x.shape[0]/10:,:]
train_set_y = set_y[set_x.shape[0]/10:]
test_set_x = set_x[0:set_x.shape[0]/10,:]
test_set_y = set_y[0:set_x.shape[0]/10]

# save h5 files
f = h5py.File('data.h5','w')
f.create_dataset('train_set_x', data=train_set_x)
f.create_dataset('train_set_y', data=train_set_y)
f.create_dataset('valid_set_x', data=valid_set_x)
f.create_dataset('valid_set_y', data=valid_set_y)
f.create_dataset('list_classes', data=list_classes)

train_set = train_set_x, train_set_y
print 'Type of train_set_x',type(train_set_x)
print 'Creating Pickle File'
train_set = train_set_x, train_set_y
valid_set = valid_set_x, valid_set_y
test_set = test_set_x, test_set_y

pickle_dataset = [train_set, valid_set, test_set]

g = gzip.open('data.pkl.gz','wb')
pickle.dump(pickle_dataset, g, protocol=2)
g.close()
