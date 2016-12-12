import scipy.misc
import numpy as np
import pickle

def get_sat_mask(image):
    return np.where( image > 0.99 , 1, 0)

data = pickle.load( open('hl.p', 'rb') )

x_source, y_source = data['train'];
x_test, y_test = data['test'];

mask = []
#Loop over all images
for i in range(0, x_test.shape[0]):
    mask = get_sat_mask(x_test[i,:,:])
    scipy.misc.imsave('itm_images/img{:4d}.png'.format(i) , x_test[i, :, :])
    scipy.misc.imsave('itm_images/mask{:4d}.png'.format(i) , mask)
