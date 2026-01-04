# Design Report

Below is the design report for my sales analysis application. 

# Introduction 

This program is a sales analysis application that takes in sales transaction information (in a .csv file), reads and then analyses this information to ultimately generate a report file (report.txt) that allows the business owner to run their business more optimally by making informed financial-decisions. The analysis from the report will contain: 

- total yearly sales and quantities sold
- breakdown of how much of each product and revenue each product generated per year, date with the amount of sales (and number of items respectively) occurring over a time-interval (i.e. over 6 months, a year, etc.) 
- predicting next weekly/monthly sales depending on user input 


# Design 

Before we explore the design of this program, it is worth noting the flow of this program in the first place. In our scenario, the program gets a csv file, reads and parses the file's transaction data, completes some analysis and finally writes the results to a .txt file. 

To meet this requirement, I decided to break the processing into groups of functions that go together by using classes, and an utility file which contains general helper functions. This way the code is kept in separate files and it's easier to read and follow.  

This program is composed of two main classes, the SalesAnalyser and AnalysisResult class. The SalesAnalyser class is responsible for reading an input file which contains sales transaction data (in a .csv format), processing/analyzing the data and outputting the result of the analysis to a .txt file. The output of the analysis is stored in the form of a list of AnalysisResult objects. The last step of writing the report iterates over the AnalysisResult objects and writes a nicely formatted report. As a result, the formatting of the report can be done independently of the processing, therefore allowing the methods implementing the processing to be tested separately.

Therefore, I was able to avoid the common mistake of consolidating all processing into few, hugely overflown functions and instead distributed the logic among many functions, where each function serves one purpose and higher level functions call lower-level functions. 

For example, top level functions e.g. sales_analyser.run_analysis() call to serve those purposes and make reference to the functions below to run the program efficiently... 
- get a list of unique products (get_unique_list()) and unique years from the input transaction data
- calls prepare_indexes() which prepares indexes to allow finding the rows in the csv file that match the unique products and years
- and then calls breakdown_of_product_and_year() which goes over all the years and products using the indexes to find matching rows so that it can then calculate the total sales and quantity sold for a specific product for a specific year

Using the layered approach, I was able to separate the user-interface aspect (getting input from user), the analysis, reading/writing components of this program.

In addition, utility.py contains general helper functions that are used on lists, for example to get a list of unique items from a list which can contain multiple/duplicate values.


# Design Highlights

My program uses classes to organize code nicely. This was a pivotal change I introduced from originally having multiple functions in one file to grouping related functions and data (member variables) into classes. Using classes made my code more readable and easier to follow. 

One aspect of my program I was particularly proud of was the way I introduced summary calculations across all the years and products found in the transaction data. In order to perform the summary calculations, the program prepares indexes for each unique product or year. This way it makes it possible to find all the sales or quantities sold matching a specific product name and year and allows statistical information to be calculated e.g. total sales or quantities sold. This approach was extended to also do calculations on other combinations e.g. get total sales for product x for a month or a week or a day or find total sales for product x on a specific week day.

# Areas for Improvement

If I had more time for this project, I would consider using the datetime module extensively, to extract the year instead of implementing it on my own (i.e. splitting the date in yyyy-mm-dd format into individual parts). Datetime could have been used to extract the day of the week, week of the year or month from a date string as well. Using this module, more customized analysis would be made possible. 

We could add functionality such that users could ask for specific information (e.g summary only for a specific product or time period) (e.g. year or month or week). On the same subject, I could incorporate the datetime module to situate a benchmark in real time and use a simple moving-averages to predict weekly sales of the following week. 

The program could also highlight the top selling product or the lowest selling product.

I could also add functionality to use the transaction id to find out if the user buys product x, which other product(s) does he/she typically also buy. This could be useful for the owner to decide on how to do promotions. 


# Lessons Learned
A few key lessons I learned through this project was realizing how much extra time gets spent upfront trying to understand how to structure a program, how to keep the data and then process it. This is even before we start writing code.

Writing a program can be an iterative process too, as we write code, we realize there are better ways to do it and we end up revising things. As I started, I was not aware about the datetime module so I started with writing a function to extract the year from the date in a string format but later found that using modules like datetime, this can be easily done. 

I also realized that writing automated tests is an involved process as I needed to spend a lot of additional time thinking of different combinations of inputs that are possible. Nonetheless, having to write tests throughout the process has many benefits including making your program more robust. Adding more automated than manual testing in the program is more effective, as testing the code, while changes are being made, becomes faster and convenient than having to run the program entirely. 