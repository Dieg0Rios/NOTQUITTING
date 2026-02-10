#NUMPY GUIDE: 
import numpy as np 

# np.array is used to initialize the array of values. 

a = np.array([[1,2],[3,6],[4,5]])

# np.ndarray is used to make a randomly innitialized array of SHAPE 1 by 2. 

b = np.ndarray([1,2])
print("This is a:", a)
print("This is b:", b)
print("This is the shape of b:", b.shape)


#Accessing an element in a numpy array: 
print("This is the first element in A:", a[0]) # will get the first index of the array 