import scipy.misc
import numpy as np

def get_sat_mask(image):
    return np.where( image > 255 , 1, 0)

data = pickle.load( open('hl.p', 'rb') )

x_source, y_source = data['train'];
x_test, y_test = data['test'];

#Loop over all images
for i in xrange(0, x_test.shape[0]):
    mask = get_sat_mask(x_test[i,:,:])
    print(mask.shape)

data = np.zeros((256,256), np.int8)
for i in range(128):
  for j in range(128):
    data[i, j] = np.random.randint(2, size=1)
scipy.misc.imsave('mask.png', data)
