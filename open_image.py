import cPickle as pickle
import numpy as np
from matplotlib import pyplot as plt
from os.path import join

with open(join('train'),'rb') as f: data_test = pickle.load(f)
images_train= data_test['data'].astype('float32')/255
print np.shape(images_train)


def affiche(im):
    plt.imshow(im.reshape(3,32,32).transpose(1,2,0))
    plt.show()
    
affiche(images_train[0])



