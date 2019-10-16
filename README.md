This Python script border_analytics.py analyse the [border crossing entry data]((https://data.transportation.gov/Research-and-Statistics/Border-Crossing-Entry-Data/keg4-3bc2)). 
Please use python3.7 for running the script.

### The approach is summarized as follow:
* First, loading the CSV file as a list of list containing Date, Measure, Border and Value. 
* Then we calculate the sum of values with a unique dict key with Date, Border and Measure.
* Next, lists called year_list and border_measure list are prepared for calculating the rolling average.
* The crucial step is calculating the rolling average. For each year, we calculate the cumulative sum of the values based on border and measure as key. The trick is that the list for rolling average contains zero because the rolling average for January is 0 according to the instruction. The 13th number in the list of rolling average should deleted.
* After sorting the results based on Border, Date, Measure and Value, the result is written to a CSV file.  

The script passed in three different test cases.

Yasheng Maimaiti 
yasheng@stanford.edu
