# DataCapture_Project
The DataCapture object accepts numbers and returns an object for querying statistics about the inputs. Specifically, the returned object supports querying how many numbers in the collection are less than a value, greater than a value, or within a range.

# CHALLENGE CONDITIONS:

o You cannot import a library that solves it instantly
o The methods add(), less(), greater(), and between() should have
constant time O(1)
o The method build_stats() can be at most linear O(n)
o Apply the best practices you know
o Share a public repo with your project

# SOLUTION:

The project was done by creating two classes. One for capturing the data from the user and
the second one was for statistics over that data based on the requirements.

The classes were stored in the Data_Project folder and in the file DataCapture.py

To run the initial conditions of the project, a main.py in the main folder has the logic that
prints in the terminal the solution. To run it, please inside the main folder run main.py

The output is the representation of the output of the three functions (less, greater and between)
print(stats.less(4))
print(stats.between(3, 6))
print(stats.greater(4))

# TESTING

Testing file is test_model.py in the main folder and to run it, it is only necessary to run in
the terminal python test_model.py
