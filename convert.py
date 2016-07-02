import cPickle
import numpy
from scipy.misc import imsave

def unpickle(file):
  fo = open(file, 'rb')
  dict = cPickle.load(fo)
  fo.close()
  return dict

xs = []
ys = []
for j in range(0):
  d = unpickle('data_'+`j+1`)
  x = d['data']
  y = d['label']
  xs.append(x)
  ys.append(y)
d = unpickle('test_data_1')
xs.append(d['data'])
ys.append(d['label'])

x = numpy.concatenate(xs)
y = numpy.concatenate(ys)

x = numpy.dstack((x[:, :1024], x[:, 1024:2048], x[:, 2048:]))

for i in range(32):
  imsave('./convnet-webapp/demo/cifar10/cifar10_batch_'+`i`+'.png', x[1000*i:1000*(i+1),:])
imsave('./convnet-webapp/demo/cifar10/cifar10_batch_'+`32`+'.png', x[1000:2000,:]) # test set

# dump the labels
L = 'var labels=' + `list(y[:33000])` + ';\n'
open('./convnet-webapp/demo/cifar10/cifar10_labels.js', 'w').write(L)
