# EXPERIMENT 2: NUMPY LIBRARY
This is a repository of Elijah David Lopez from 2-ECEB for the course ECE2112 for Experiment Number 2

### I.OBJECTIVE
This experiment aims to identify the functions incorporated in Numpy Library and apply and use these different codes in creating a Python program.

### II. INSTRUCTIONS

1. **__NORMALIZATION PROBLEM:__** Normalization is one of the most basic preprocessing techniques in data analytics. This involves a centering and scaling process. Centering means subtracting the data from the mean, and scaling means dividing by its standard deviation. Mathematically, normalization can be expressed as:
![image](https://github.com/user-attachments/assets/7f220dab-585f-41b5-97ba-415286c8c492)

Said Problem was solved by writing the following lines of codes:
![image](https://github.com/user-attachments/assets/1eda9dc7-e7f5-48e6-8df9-132067dade6a)

Some insights: It used a random array, which was placed in a nested loop to run the operation of normalization depicted in the above image, and placed within an empty array, which was the product being asked for by the problem.


# ________________________________________________________________________


2. **__DIVISIBLE BY 3 PROBLEM:__** Create the following 10 x 10 ndarray which are the squares of the first 100 positive integers. From this ndarray, determine all the elements that are divisible by 3. Save the result as div_by_3.npy

Said Problem was solved by writing the following lines of codes:
![image](https://github.com/user-attachments/assets/9b999b8e-402a-4631-8c5f-77843b18ed37)

Some Insights: This was a two-part code. The first would fill the initial 10x10 with the squares of the first 100 numbers, done with a counter multiplying within a nested loop. Then, another nested loop is run, which would check along the entire array, divisible by 3 (depicted with the modulo operation within an if-else statement). If it detects one, it would add one to the counter, which also happens to be the index of the array being filled with numbers divisible by 3, which was the array saved for it is the product asked by the problem.
