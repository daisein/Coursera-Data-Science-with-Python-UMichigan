# # # # # # # # # # # # # # # # ## # # # # # # # # # # # # #
# Reading and Writing CSV files
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import csv

def read_write_csv():
    with open('mpg.csv') as csvfile:
        mpg = list(csv.DictReader(csvfile))

    # print(mpg[:3])
    # mpg[:3] # The first three dictionaries in our list.
    # print(mpg[0].keys())

    cty_fuel = sum(float(d['cty']) for d in mpg) / len(mpg)
    hwy_fuel = sum(float(d['hwy']) for d in mpg) / len(mpg)
    cylinders = set(d['cyl'] for d in mpg)
    # print(cylinders)

    CtyMpgByCyl = []

    for c in cylinders: # iterate over all the cylinder levels
        summpg = 0
        cyltypecount = 0
        for d in mpg: # iterate over all dictionaries
            if d['cyl'] == c: # if the cylinder level type matches,
                summpg += float(d['cty']) # add the cty mpg
                cyltypecount += 1 # increment the count
        CtyMpgByCyl.append((c, summpg / cyltypecount)) # append the tuple ('cylinder', 'avg mpg')

    CtyMpgByCyl.sort(key=lambda x: x[0])
    # print(CtyMpgByCyl)

    vehicleclass = set(d['class'] for d in mpg) # what are the class types
    # print(vehicleclass)

    HwyMpgByClass = []

    for t in vehicleclass: # iterate over all the vehicle classes
        summpg = 0
        vclasscount = 0
        for d in mpg: # iterate over all dictionaries
            if d['class'] == t: # if the cylinder amount type matches,
                summpg += float(d['hwy']) # add the hwy mpg
                vclasscount += 1 # increment the count
        HwyMpgByClass.append((t, summpg / vclasscount)) # append the tuple ('class', 'avg mpg')

    HwyMpgByClass.sort(key=lambda x: x[1])
    print(HwyMpgByClass)

# read_write_csv()



# # # # # # # # # # # # # # # # ## # # # # # # # # # # # # #
# The Python Programming Language: Dates and Times
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import datetime as dt
import time as tm

def dates_and_times():
    tm.time()
    # print(tm.time())

    dtnow = dt.datetime.fromtimestamp(tm.time())
    print(dtnow)
    dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second # get year, month, day, etc.from a datetime

    delta = dt.timedelta(days = 100) # create a timedelta of 100 days
    print(delta)

    today = dt.date.today()
    today - delta # the date 100 days ago
    print(today - delta)
    today > today-delta # compare dates
    print(today > today-delta)

# dates_and_times()


# # # # # # # # # # # # # # # # ## # # # # # # # # # # # # #
# The Python Programming Language: Objects and map()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def objects_and_map():

    class Person:
        department = 'School of Information' #a class variable

        def set_name(self, new_name): #a method
            self.name = new_name
        def set_location(self, new_location):
            self.location = new_location

    person = Person()
    person.set_name('Christopher Brooks')
    person.set_location('Ann Arbor, MI, USA')
    print('{} live in {} and works in the department {}'.format(person.name, person.location, person.department))

    store1 = [10.00, 11.00, 12.34, 2.34]
    store2 = [9.00, 11.10, 12.34, 2.01]
    cheapest = map(min, store1, store2)
    for item in cheapest:
        print(item)

# objects_and_map()


# # # # # # # # # # # # # # # # ## # # # # # # # # # # # # #
# The Python Programming Language: Lambda and List Comprehensions
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def lambda_and_list():
    my_function = lambda a, b, c : a + b
    print(my_function(1, 2, 3))

    my_list = []
    for number in range(0, 1000):
        if number % 2 == 0:
            my_list.append(number)
    # print(my_list)

    # Now the same thing but with list comprehension.
    my_list = [number for number in range(0,1000) if number % 2 == 0]
    print(my_list)

# lambda_and_list()


# # # # # # # # # # # # # # # # ## # # # # # # # # # # # # #
# The Python Programming Language: Numerical Python (NumPy)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import numpy as np

def np_functions():

    print('')
    print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
    print('Creating Arrays')
    print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
    print('')
    # Create a list and convert it to a numpy array
    mylist = [1, 2, 3]
    x = np.array(mylist)
    # print(x)

    # Or just pass in a list directly
    y = np.array([4, 5, 6])
    # print(y)

    # Pass in a list of lists to create a multidimensional array.
    m = np.array([[7, 8, 9], [10, 11, 12]])
    print(m)

    # Use the shape method to find the dimensions of the array. (rows, columns)
    print(m.shape)

    # `arange` returns evenly spaced values within a given interval.

    n = np.arange(0, 30, 2) # start at 0 count up by 2, stop before 30
    print(n)

    # `reshape` returns an array with the same data with a new shape.
    n = n.reshape(3, 5) # reshape array to be 3x5
    print(n)

    # `linspace` returns evenly spaced numbers over a specified interval.
    o = np.linspace(0, 4, 9) # return 9 evenly spaced values from 0 to 4
    print(o)

    # `resize` changes the shape and size of array in-place.
    o.resize(3, 3)
    print(o)

    # `ones` returns a new array of given shape and type, filled with ones.
    print(np.ones((3, 2)))

    # `zeros` returns a new array of given shape and type, filled with zeros.
    print(np.zeros((2, 3)))

    # `eye` returns a 2-D array with ones on the diagonal and zeros elsewhere.
    print(np.eye(3))

    # `diag` extracts a diagonal or constructs a diagonal array.
    print(np.diag(y))

    # Create an array using repeating list (or see `np.tile`)
    print(np.array([1, 2, 3] * 3))

    # Repeat elements of an array using `repeat`.
    print(np.repeat([1, 2, 3], 3))



# def combining_arrays():
    print('')
    print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
    print('Combining Arrays')
    print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
    print('')

    p = np.ones([2, 3], int)
    print(p)

    # Use `vstack` to stack arrays in sequence vertically (row wise).
    print(np.vstack([p, 2*p]))

    # Use `hstack` to stack arrays in sequence horizontally (column wise).
    print(np.hstack([p, 2*p]))

    # combining_arrays()

    # Operations
    print('')
    print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
    print('Operations')
    print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
    print('')


    # Use `+`, `-`, `*`, `/` and `**` to perform element wise addition, subtraction, multiplication, division and power.

    print(x + y) # elementwise addition     [1 2 3] + [4 5 6] = [5  7  9]
    print(x - y) # elementwise subtraction  [1 2 3] - [4 5 6] = [-3 -3 -3]

    print(x * y) # elementwise multiplication  [1 2 3] * [4 5 6] = [4  10  18]
    print(x / y) # elementwise divison         [1 2 3] / [4 5 6] = [0.25  0.4  0.5]

    print(x**2) # elementwise power  [1 2 3] ^2 =  [1 4 9]

    print(x.dot(y)) # dot product  1*4 + 2*5 + 3*6

    z = np.array([y, y**2])
    print(len(z)) # number of rows of array

    # Let's look at transposing arrays. Transposing permutes the dimensions of the array.
    z = np.array([y, y**2])
    print(z)

    # The shape of array `z` is `(2,3)` before transposing.
    print(z.shape)

    # Use `.T` to get the transpose.
    z.T
    print(z.T)

    # The number of rows has swapped with the number of columns.
    z.T.shape

    # Use `.dtype` to see the data type of the elements in the array.
    print(z.dtype)

    # Use `.astype` to cast to a specific type.
    z = z.astype('f')
    print(z.dtype)


    print('')
    print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
    print('Math Functions')
    print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
    print('')

    # Numpy has many built in math functions that can be performed on arrays.
    a = np.array([-4, -2, 1, 3, 5])
    print('sum',a.sum())
    print('max',a.max())
    print('min',a.min())
    print('mean',a.mean())
    print('std',a.std())

    # `argmax` and `argmin` return the index of the maximum and minimum values in the array.

    print('argmax', a.argmax())
    print('argmin', a.argmin())

    print('')
    print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
    print('Indexing/ Slicing')
    print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
    print('')

    s = np.arange(13)**2
    print(s)

    # Use bracket notation to get the value at a specific index. Remember that indexing starts at 0.

    print(s[0], s[4], s[-1])

    # Use `:` to indicate a range. `array[start:stop]`
    # Leaving `start` or `stop` empty will default to the beginning/end of the array.
    print(s[1:5])

    # Use negatives to count from the back.
    print(s[-4:])


    # A second `:` can be used to indicate step-size. `array[start:stop:stepsize]`

    # Here we are starting 5th element from the end, and counting backwards by 2 until the beginning of the array is reached.
    print(s[-5::-2])

    # Let's look at a multidimensional array.
    r = np.arange(36)
    r.resize((6, 6))
    print(r)

    # Use bracket notation to slice: `array[row, column]`
    print(r[2, 2])

    # And use : to select a range of rows or columns
    print(r[3, 3:6])

    # Here we are selecting all the rows up to (and not including) row 2, and all the columns up to (and not including) the last column.
    print(r[:2, :-1])

    # This is a slice of the last row, and only every other element.
    print(r[-1, ::2])

    # We can also perform conditional indexing. Here we are selecting values from the array that are greater than 30. (Also see `np.where`)
    print(r[r > 30])

    # Here we are assigning all values in the array that are greater than 30 to the value of 30.
    r[r > 30] = 30
    print(r)

    print('')
    print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
    print('Copying Data')
    print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
    print('')

    # Be careful with copying and modifying arrays in NumPy!
    # `r2` is a slice of `r`

    r2 = r[:3,:3]
    print(r2)

    # Set this slice's values to zero ([:] selects the entire array)
    r2[:] = 0
    print(r2)

    # `r` has also been changed!
    print(r)

    # To avoid this, use `r.copy` to create a copy that will not affect the original array
    r_copy = r.copy()
    print(r_copy)

    # Now when r_copy is modified, r will not be changed.
    r_copy[:] = 10
    print(r_copy, '\n')
    print(r)

    print('')
    print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
    print('Iterating Over Arrays')
    print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
    print('')

    # Let's create a new 4 by 3 array of random numbers 0-9.

    test = np.random.randint(0, 10, (4,3))
    print(test)

    # Iterate by row:

    for row in test:
        print(row)

    # Iterate by index:
    for i in range(len(test)):
        print(test[i])

    # Iterate by row and index:
    for i, row in enumerate(test):
        print('row', i, 'is', row)

    # Use `zip` to iterate over multiple iterables.
    test2 = test**2
    print(test2)

    for i, j in zip(test, test2):
        print(i,'+',j,'=',i+j)

# np_functions()


def quiz():
    r = np.arange(36)
    r.resize((6, 6))

    print(r.reshape(36)[::7])
    print(r[2:4,2:4])


quiz()
