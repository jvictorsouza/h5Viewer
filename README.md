# h5Viewer

This is a repository that contains code written in python to view and save compressed images in .h5 or .hdf5 format. An h5 file is a data file saved in the Hierarchical Data Format (HDF) designed to store and organize large amounts of data.

## Prerequisites
  * Python 3
  * OpenCV 3.4.4
  * h5py==2.10.0
  * Numpy==1.16.2
  * Keyboard==0.13.4
 
 PS.: Other versions of these libraries may work properly. 
  
 ### Example of execution:
 $ python main.py -p patient_images_lowres.h5 -sv n -sw y
 
 The first argument is the path to the file .h5, the second is the option to save the images and the third is the option to show the images. 
 
 ### Output
 The images will be save in a paste 'data'.
 
