# Experiment 4 - DATA WRANGLING AND DATA VISUALIZATION
## I. Objectives
### The objective of the experiment is to identify the codes and functions that can be used to clean and visualize data and to be able to apply these codes and functions to create a Python program that can be used in data wrangling and data visualization.

## II. Problems
For this experiment, an Excel file was imported to use as the data frame for the two problems using the pd.read_excel() function and set inside the variable brd

### Problem 1: 1. Create the following data frames based on the format provided:
Example: Vis = [“Name”, “Gender”, “Track”, “Math<70”]; hometown is constant as the Visayas

a. Filename: Instru = [“Name”, “GEAS”, “Electronics >70”]; where the track is constant as Instrumentation and Hometown Luzon

For this set, it uses a basic brd.loc function to locate a row that follows multiple conditions: the student is from Instrumentation for Track, their Hometown is Luzon, and then their grade for Math is lower than 70. This problem was solved using the code:

![image](https://github.com/user-attachments/assets/862d5657-be9e-4b28-b5d9-d30462ebb346)

and would result to a dataframe of:

![image](https://github.com/user-attachments/assets/ee0c1243-374a-45ac-a9db-ccfd369d0b05)


b. Filename: Mindy = [ “Name”, “Track”, “Electronics”, “Average >=55”]; where hometown is constant as Mindanao and gender Female

This problem, requires making a new column at the bird data frame for the average of values of all the grades, which was done using brd['Average'] = brd[[labels]].mean(axis=1). The axis has to be one as it is the mean of the values in the row you are getting the average of. Then, using the same .loc function to locate the rows that meet the conditions being of female are the only one getting checked, and from Mindanao as their hometown and specifying that only the Name, Track, Electronics, and Average columns be displayed. 
  
  This problem was solved by using the following code:
  
  ![image](https://github.com/user-attachments/assets/8ae00568-b236-413f-9006-1f26b1afcee6)

  and results to the dataframe:
  
  ![image](https://github.com/user-attachments/assets/19a5303f-39e8-43bf-b2a8-2ce3988dfc48)


#### ______________________________________________________________________________________

### Problem 2: Create a visualization that shows how the different features contributes to average grade. Does
chosen track in college, gender, or hometown contributes to a higher average score?

The graphical representation used for the data is bar graphs, which are programmed using the mathplotlib.pyplot functions, mostly using .figure to configure the size, .bar for the kind of graph, and .title for the title of the graph, and the others use .xtick to rotate the label text for the x categories so that it won't over lap. The following are the codes and the graph produced by such codes

Code: ![image](https://github.com/user-attachments/assets/0707eff3-bdc0-4ec5-9d48-917498057538)
Graph: ![image](https://github.com/user-attachments/assets/76e01e2f-4e5a-44cd-929d-22b4ad996289)

This graph shows that Microelectronics seems to have the highest average, followed by Communications, and then by Instrumentations.

Code: ![image](https://github.com/user-attachments/assets/2abe2f32-4b5a-48d9-b834-b2b5651ec8d5)
Graph: ![image](https://github.com/user-attachments/assets/24f06003-a9f6-4233-9147-a76b8c332661)

Meanwhile, this graph shows that it is the female students that get the higher average, probably higher scores than males as well.

Code:![image](https://github.com/user-attachments/assets/c4cec91c-3e0d-47d4-8df4-657d2071cc5f)
Graph: ![image](https://github.com/user-attachments/assets/183d6b9e-82cf-400f-b05b-297441d8fc47)

Finally, this graph shows that the high average comes from Luzon, and then followed by those that came from Mindanao, and then lastly, by those from Visayas.



