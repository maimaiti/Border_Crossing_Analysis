This is my solution for Insight data engineering coding challenge called [Border Crossing Analysis](https://github.com/InsightDataScience/border-crossing-analysis). 
Please use python3.7 for running the script.

### The approach is summarized as follow:
* First, loading the csv file as a nested list which only contains Date, Measure, Border and Value. 
* Then we calculate the sum of value using a unique dict key of Date, Border and Measure.
* Next, lists called year_list and border_measure_list are prepared for calculating the rolling average.
* The crucial step is calculating the rolling average. For each year, we calculate the cumulative sum of the values based on border and measure as dict key. The trick is that the list for rolling average already contains zero because the rolling average for January is 0 according to the instruction. The 13th number in the list of rolling average should deleted.
* After sorting the results based on Border, Date, Measure and Value, the result is written to a CSV file.  

The script passed in three different test cases.

Yasheng Maimaiti 
yasheng@stanford.edu
