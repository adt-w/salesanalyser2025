
# How to Test

In order to ensure this application works as expected, we need to add automated testing (using pytest) for functions/methods implemented in the sales_analysr.py and utility.py. We will also use manual testing where the full program will be run given different user inputs and verification will be done on the output. 

# Automated Testing

The program takes a csv file as input, completes some analysis and outputs the results in a report.txt file. As major code lies in sales_analyser.py and utility.py, there are automated tests in test_sales_analyser.py and test_utility.py that validate the logic of our program. The details of the tests are listed below:

Testing sales_analyser.py (test_sales_analyser.py)
- Basic automated testing
    - test_read_valid_columns
        - this test checks the loading of the data from an existing csv file where there are no problems with the contents in the file 
    - test_get_unique_years
        - this test simply checks if a unique years list we have provided will have been generated correctly given valid information in our csv file 
    - test_prepare_indexes
        - this test focuses on outputting the indexes where our unique products and unique years are located given valid data from our csv file from our read_data method
    - test_breakdown_of_product_and_year
        - this test focuses on mapping similar indexes where both our unique years and unique products are found 

Testing utility.py (test_utility.py)
- Basic automated testing
    - test_get_unique_list_with_duplicates
        - this test checks whether the get_unique_list function will properly remove all duplicates given an initial list consisting of them 
    - test_get_valid_extraction_of_year
        - this test checks whether the extract_year function will accurately split a string and store only the year value for each entry from our original date list in our SalesAnalysis class
    - test_valid_common_items
        - this test checks if the function get_common_items accurately finds the common items which exist in two separate lists 
        (note: this function was a helper function for the breakdown_of_product_and_year() method)

    
# Manual Testing 

This application also requires user input to generate the report.txt file in the beginning of the program. The goal of manual testing is to have the user run the program from a set of different inputs and check whether the output is as expected or not. We use manual testing for cases where user input is required and for validating the report.txt file, as they can not be covered using automated testing. The use cases covered by manual testing include:

- user providing a valid csv file (with different combinations of transaction data, e.g. multiple products, multiple years, etc.)
- user providing a non-existing csv file 
- user providing an empty csv file (csv file with nothing in it)
- user providing a csv file with only headers
- user providing an existing csv files with errors in data 

**Note: Validating report.txt file is very tedious and requires a lot of manual computations which would need to be verified individually.