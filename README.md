# Experiment # 3
## Python Data Analysis

### I. Objectives
This experiment aims to identify the codes incorporated into a Python Library, specifically Pandas. It is also the aim of this experiment to allow us to explore how we can use and apply the different codes and functions in creating a Python program using
Pandas Library.

### II. Problems 

For this set of problems, a .csv file, 'cars.csv', is required to complete the procedures. 

#### Problem 1: Save your file as Surname_Pandas-P1.py
Using knowledge obtained from the experiment and demonstrations:
a. Load the corresponding .csv file into a data frame named cars using pandas
b. Display the first five and last five rows of the resulting cars.

This problem requires the loading of the .csv file, which was done using pd.read_csv() operation and is saved in one variable, cars,  and then using .tail and .head function to display the two extremes, the first and last five values or rows of the tabled values. Using the print code was needed to separate the tail and the head functions, as it results in only the latest function called running without print, as demonstrated in the last part of the code.

![image](https://github.com/user-attachments/assets/a0bf0e8b-ba00-43fb-8c47-24a0bdb2a77e)


#### _________________________________________________________________________________________________________


#### Problem 2: Save your file as Surname_Pandas-P2.py
Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and
indexing operations.
a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.
b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4
Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have

This problem uses the same .csv saved in the variable cars as dataframe for its procedure. Firstly, it requires the display of the first five rows and only the odd-numbered columns. This was performed by using an array fed by a loop that would fill them with numbers that satisfy the condition for both the rows and columns and using those arrays for the parameters of the cars.iloc() function.

![image](https://github.com/user-attachments/assets/72db5abb-01b7-4a02-a955-6464b33b9242)

The next part of the problem asks for specific values, the first being the row of values, displaying all columns from the model Mazda RX4

![image](https://github.com/user-attachments/assets/7da65325-f61d-4ad3-8ae2-e8b54007799a)

This brings us to the next part. The next part only asks for the model and cylinder values of the model, 'Camaro Z28'

![image](https://github.com/user-attachments/assets/68a39660-329a-44c8-acc8-273aaf116e2f)

The last part then asks for the table displaying the model, cylinders, and gears of three models, which was compiled in a list and ran a while loop on to put them on the cars.iloc as parameters and using print to print all the table values and not just the latest

![image](https://github.com/user-attachments/assets/b431acc0-fb55-4fe3-abf6-59a52cda4a6f)
