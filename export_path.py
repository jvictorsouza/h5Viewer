import cv2
import h5py
import os
import numpy as np
import process_image


def directory_images(path, save, show):
    try:
        f = h5py.File(path, 'r')
    except IOError as err:
        print('[INFO] File .h5 not found.')
        exit()

    keys = f.keys()
    for k in keys:  # PASTAS PRINCIPAIS
        p = '{}'.format(k)
        try:
            os.mkdir('data/' + k)
            print("Directory ", k, " Created ")
        except FileExistsError:
            print("Directory ", k, " already exists")
        try:
            shape1 = f[k].shape
            process_image.PI(f, p, shape1, save, show)

        except AttributeError:
            paths1 = list(f[k])
            for p1 in paths1:
                p = '{}/{}'.format(k, p1)
                try:
                    os.mkdir('data/' + p)
                    print("Directory ", p1, " Created ")
                except FileExistsError:
                    print("Directory ", p1, " already exists")
                try:
                    shape2 = f[p].shape
                    process_image.PI(f, p, shape2, save, show)
                except AttributeError:
                    paths2 = list(f[p])
                    for p2 in paths2:
                        p = '{}/{}'.format(p, p2)
                        try:
                            os.mkdir('data/' + p)
                            print("Directory ", p2, " Created ")
                        except FileExistsError:
                            print("Directory ", p2, " already exists")
                        try:
                            shape3 = f[p].shape
                            process_image.PI(f, p, shape3, save, show)
                        except AttributeError:
                            print("[INFO] The .h5 files exceed the limit")
                            exit()

    f.close()
    exit()