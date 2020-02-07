This is my solution for Insight data engineering coding challenge called [Border Crossing Analysis](https://github.com/InsightDataScience/border-crossing-analysis). 
Please use python3.7 for running the script.

### The approach is summarized as follows:
* First, loading the csv file as a list which only contains Date, Measure, Border and Value columns from csv. 
* Then we calculate the sum of value using a unique dict key of Date, Border and Measure.
* Next, the lists called year_list and border_measure_list are prepared for calculating the rolling average.
* The crucial step is calculating the rolling average. To do this, we calculate the cumulative sum of the values based on border and measure as dict key for each year. One trick here is that the list for rolling average already contains zero because the rolling average for January is 0 according to the instruction, and thus the 13th number in the list of rolling average should be deleted.
* After sorting the results based on Border, Date, Measure and Value, the result is written to a csv file.  

The script passed in three different test cases.
