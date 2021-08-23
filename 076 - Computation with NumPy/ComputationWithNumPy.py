# Import Statements

import numpy as np

import matplotlib.pyplot as plt
from scipy import misc # contains an image of a racoon!
from PIL import Image # for reading image files

# Understanding NumPy's ndarray

NumPy's most amazing feature is the **powerful** ndarray.

<img src="https://i.imgur.com/1IUqnxX.png" width=200>

#### 1-Dimensional Arrays (Vectors)

# Create new ndarray from scatch
my_array = np.array([1.1, 9.2, 8.1, 4.7])

# Show rows and columns
my_array.shape

# Accessing elements by index
my_array[2]

# Show dimensions of an array
my_array.ndim


#### 2-Dimensional Arrays (Matrices)

array_2d = np.array([[1, 2, 3, 9], 
                     [5, 6, 7, 8]])

print(f'array_2d has {array_2d.ndim} dimensions')
print(f'Its shape is {array_2d.shape}')
print(f'It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns')
print(array_2d)

# Access the 3rd value in the 2nd row
array_2d[1,2]

# Access all the values in the first row
array_2d[0, :]

#### N-Dimensional Arrays (Tensors)

**Challenge**: 
* How many dimensions does the array below have? 
* What is its shape (i.e., how many elements are along each axis)?
* Try to access the value `18` in the last line of code.
* Try to retrieve a 1 dimensional vector with the values `[97, 0, 27, 18]`
* Try to retrieve a (3,2) matrix with the values `[[ 0,  4], [ 7,  5], [ 5, 97]]`

*Hint*: You can use the `:` operator just as with Python Lists.

mystery_array = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],
                        
                         [[7, 86, 6, 98],
                          [5, 1, 0, 4]],
                          
                          [[5, 36, 32, 48],
                           [97, 0, 27, 18]]])

# Note all the square brackets!

print(f'We have {mystery_array.ndim} dimensions')
print(f'The shape is {mystery_array.shape}')

# Axis 0: 3rd element. Axis 1: 2nd Element. Axis 3: 4th Element
mystery_array[2, 1, 3]

# Retrieve all the elements on the 3rd axis that are at
# position 2 on the first axis and position 1 on the second axis.
mystery_array[2, 1, :]

# All the first elements on axis number 3
mystery_array[:, :, 0]

# NumPy Mini-Challenges

#### **Challenge 1**: Use [`.arange()`](https://numpy.org/devdocs/reference/generated/numpy.arange.html)to createa a vector `a` with values ranging from 10 to 29. You should get this:

`print(a)`

`[10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29]`

a = np.arange(10,30)
print(a)

#### **Challenge 2**: Use Python slicing techniques on `a` to:
* Create an array containing only the last 3 values of `a`
* Create a subset with only the 4th, 5th, and 6th values
* Create a subset of `a` containing all the values except for the first 12 (i.e., `[22, 23, 24, 25, 26, 27, 28, 29]`)
* Create a subset that only contains the even numbers (i.e, every second number)

# last 3 values
a[-3:]

# interval of values
a[3:6]

# all the values except the first 12
a[12:]

# every second value (all the even numbers)
a[::2]

#### **Challenge 3**:Reverse the order of the values in `a`, so that the first element comes last:

`[29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13,
       12, 11, 10]`


If you need a hint, you can check out this part of the [NumPy beginner's guide](
https://numpy.org/devdocs/user/absolute_beginners.html#how-to-reverse-an-array)

np.flip(a)

a[::-1]

#### **Challenge 4**: Print out all the indices of the non-zero elements in this array: [6,0,9,0,0,5,0]

b = np.array([6,0,9,0,0,5,0])
nz_indices = np.nonzero(b)
nz_indices # note this is a tuple

#### **Challenge 5**: Use NumPy to generate a 3x3x3 array with random numbers

Hint: Use the [`.random()` function](https://numpy.org/doc/stable/reference/random/index.html?highlight=random#module-numpy.random)

from numpy.random import random
z = random((3,3,3))
z

z = np.random.random((3,3,3)) # without an import statement
print(z.shape)
z

#### **Challenge 6**: Use [`.linspace()`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) to create a vector `x` of size 9 with values spaced out evenly between 0 to 100 (both included).

x = np.linspace(0, 100, num=9)
print(x)
x.shape

#### **Challenge 7**: Use [`.linspace()`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) to create another vector `y` of size 9 with values between -3 to 3 (both included). Then plot `x` and `y` on a line chart using Matplotlib.

y = np.linspace(start=-3, stop=3, num=9)
y

plt.plot(x, y)
plt.show()

#### **Challenge 8**: Use NumPy to generate an array called `noise` with shape 128x128x3 that has random values. Then use Matplotlib's [`.imshow()`](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.imshow.html) to display the array as an image. 

noise = np.random.random((128,128,3))
print(noise.shape)
plt.imshow(noise)

# Linear Algebra with Vectors

v1 = np.array([4, 5, 2, 7])
v2 = np.array([2, 1, 3, 3])

v1 + v2

# Python Lists vs ndarrays
list1 = [4, 5, 2, 7]
list2 = [2, 1, 3, 3]

list1 + list2

v1 * v2

# list1 * list2 # error!

# Broadcasting and Scalars


array_2d = np.array([[1, 2, 3, 4], 
                     [5, 6, 7, 8]])

print(f'Dimensions: {array_2d.ndim}')
print(f'Shape: {array_2d.shape}')

array_2d + 10

array_2d * 5

# Matrix Multiplication with @ and .matmul()

<img src=https://i.imgur.com/LCdhmi8.png width=350>

a1 = np.array([[1, 3],
               [0, 1],
               [6, 2],
               [9, 7]])

b1 = np.array([[4, 1, 3],
               [5, 8, 5]])

print(f'{a1.shape}: a has {a1.shape[0]} rows and {a1.shape[1]} columns.')
print(f'{b1.shape}: b has {b1.shape[0]} rows and {b1.shape[1]} columns.')
print('Dimensions of result: (4x2)*(2x3)=(4x3)')

**Challenge**: Let's multiply `a1` with `b1`. Looking at the wikipedia example above, work out the values for c12 and c33 on paper. Then use the [`.matmul()`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html) function or the `@` operator to check your work. 

c = np.matmul(a1, b1)
print(f'Matrix c has {c.shape[0]} rows and {c.shape[1]} columns.')
c

a1 @ b1

# Manipulating Images as ndarrays


img = misc.face()

plt.imshow(img)

**Challenge**: What is the data type of `img`? Also, what is the shape of `img` and how many dimensions does it have? What is the resolution of the image?

img

type(img)

img.shape

img.ndim

**Challenge**: Convert the image to black and white. The values in our `img` range from 0 to 255. 
* Divide all the values by 255 to convert them to sRGB, where all the values are between 0 and 1. 
* Next, multiply the sRGB array by the `grey_vals` to convert the image to grey scale. 
* Finally use Matplotlib's [`.imshow()`](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.imshow.html) together with the colormap parameter set to gray `cmap=gray` to look at the results. 

grey_vals = np.array([0.2126, 0.7152, 0.0722])

sRGB_array = img / 255

img_gray = sRGB_array @ grey_vals
# or use
img_gray = np.matmul(sRGB_array, grey_vals)

plt.imshow(img_gray, cmap='gray')

plt.imshow(img_gray)

**Challenge**: Can you manipulate the images by doing some operations on the underlying ndarrays? See if you can change the values in the ndarray so that:

1) You flip the grayscale image upside down

<img src=https://i.imgur.com/r36CigD.png>

2) Rotate the colour image

<img src=https://i.imgur.com/IiNylco.png>

3) Invert (i.e., solarize) the colour image. To do this you need to converting all the pixels to their "opposite" value, so black (0) becomes white (255).

<img src=https://i.imgur.com/cfFbuex.png>

#### Challenge Solutions

a1

np.flip(a1)

plt.imshow(np.flip(img_gray), cmap='gray')

print(a1)
print('a1 array rotated:')
np.rot90(a1)

plt.imshow(np.rot90(img))

solar_img = 255 - img
plt.imshow(solar_img)

# Use your Own Image!

file_name = 'yummy_macarons.jpg'

#### Use PIL to open 

my_img = Image.open(file_name)

img_array = np.array(my_img)

img_array.ndim

img_array.shape

plt.imshow(img_array)

plt.imshow(255-img_array)
