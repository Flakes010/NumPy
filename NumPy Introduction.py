import numpy as np


a = np.array([1,2,3], dtype='int8')   #1 Dimensional Array (you can also set a datatype to your array)
b = np.array([[1,2,3,4,5,6,7,8,9],[10,11,12,13,14,15,16,17,18]])   #2 Dimensional Array
c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]]) #   3 Dimensinal Array
a.ndim   #Get Dimension
a.shape   #Get How many rows and columns (a.shape -> 3, b.shape -> 2(rows), 9(columns))
a.dtype   #Get the datatype (ex. int32)
a.itemsize   #Get the bytes (4 bits = 1byte, 16 bites = 4bytes)

b[1,6] or b[1,-3]   #Get a specific number [row, column]
b[1, :]   #Get a specific row
b[:, 5]   #Get a specific column
b[0, 0:9:3] # [startindex:endindex:stepsize]
b[0,3] = 6   #Change a specific number
b[:, 8] = [10,19]   #Change a specific column or row (but the numberquantity should match together)

d = np.zeros((2,3), dtype='int32')   #Fills with zeros
e = np.ones((3,3))   #Fills with ones
f = np.full((3,3), 99)   #Fills with the given number
g = np.random.random_sample(a.shape)   #Random decimal Numbers
h = np.random.randint(1,20, size=(3,3))   #Random Integers
i = np.identity(4)   #Identity Matrix
j = np.array([[1,2,3]])
k = np.repeat(j, 3, axis=0)   #Syntax -> np.repeat(which array, how many times)

a += 2
a -= 2
a *= 2
a //= 2
a + j

np.min(b)
np.max(b)
np.sum(b)

l = a.copy()
after = l.reshape((3,1))   #Reshaping
array1 = np.array([1,2,3,4])
array2 = np.array([5,6,7,8])
stacked_array = np.vstack((array1,array2))   #Verticaly Stack

filedata = np.genfromtxt('data.txt', delimiter=',')   #Loading Data from File
filedata = filedata.astype('int32')

filedata[filedata > 50]   #Prints only the numbers greater than 50
jk = np.any(filedata > 50, axis=0)
jl = np.any(~((filedata > 50) & (filedata < 100)), axis=0)   #~ = reverse
a[[0,2]]   #You can ask arrays with lists
