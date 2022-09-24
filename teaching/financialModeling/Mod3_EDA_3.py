# In this exercise, you will write a function that takes as input a 1D array of data
# and then returns the x and y values of the ECDF. You will use this function over and over again
# throughout this course and its sequel.
# ECDFs are among the most important plots in statistical analysis.
# In this exercise, you will write a function that takes as input a 1D array of data and then returns the
# x and y values of the ECDF. You will use this function over and over again
# throughout this course and its sequel. ECDFs are among the most important plots in statistical analysis.

'''
Define a function with the signature ecdf(data). Within the function definition,

    - Compute the number of data points, n, using the len() function.
    - The x-values are the sorted data. Use the np.sort() function to perform the sorting.
    - The y-data of the ECDF go from 1/n to 1 in equally spaced increments.
      You can construct this using np.arange().
      Remember, however, that the end value in np.arange() is not inclusive.
      Therefore, np.arange() will need to go from 1 to n+1. Be sure to divide this by n.
    - The function returns the values x and y.
'''
def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = _(_)

    # x-data for the ECDF: x
    x = _(_)

    # y-data for the ECDF: y
    y = _(_, _) / n

    return x, y

#generate 150 points from N(0,1)

# Compute ECDF for data: x_vers, y_vers
_ , _ = _ ( _ )

# Generate plot

# Label the axes

# Display the plot
