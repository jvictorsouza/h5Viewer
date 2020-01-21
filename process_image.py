import numpy as np
import cv2
import keyboard
import h5py

def normalize_img(v):
    v = (v - v.min())/(v.max() - v.min())
    return (v*255).astype(np.uint8)

def PI(f, p, shape, save, show):
    for i in range(0, shape[0]):
        imgOut = normalize_img(f[p][i][:])
        if save == 'y':
            cv2.imwrite('data/' + p + '/{}.png'.format(i), imgOut)

        if show == 'y':
            print('[INFO] Image {}/{}'.format(i, shape[0]))
            cv2.imshow("Image", imgOut)
            if keyboard.is_pressed('Esc'):
                exit()
            cv2.waitKey(0)
