# Test Coverage

In addition to the basic automated pytesting covered in the how_to_test.md, there are many more cases for boundary/edge cases that were covered by automated testing. They will be covered in this file.

It is worth noting that the command for running both pytest files is:
- `pytest --verbose test_sales_analyser.py` 
- `pytest --verbose utility.py`

sales_analyser.py 
- Extended automated testing
    - test_read_empty_csv
        - this test serves as a boundary case where we test to see if a ValueError gets raised when having to process an empty csv file in the read_data() method 
    - test_read_header_only_csv
        - this test serves as a boundary case where we test to see if a ValueError gets raised when having to process a header_only csv file in the read_data() method 
    - test_read_data_invalid_amount
        - this test serves as a boundary case where we test to see if a ValueError gets raised when having to process a properly formatted csv file with invalid entries (e.g. writing 'abc' under the 'amount' category instead of a number) in the read_data() method 
    - test_read_data_invalid_quantity
        - this test serves as a boundary case where we test to see if a ValueError gets raised when having to process a properly formatted csv file with invalid entries (e.g. empty value under the 'count') in the read_data() method 

utility.py
- Extended automated testing 
    - test_get_unique_list_with_empty_list
        - this test checks for a boundary case where an empty list is provided instead of one with duplicates in it (and would return the empty list as a result)
    - test_no_common_items
        - this test checks for a boundary case for which there are no common items between the two lists passed in the get_common_items function (and as a result should be left empty afterwards)
    - test_common_items_with_empty_list_single
        - this test checks for a boundary case where the input to our get_common_items function contains one empty list, and one populated list, where the result list is empty
    - test_common_items_with_empty_list_both
        - this test checks for a boundary case where the input to our get_common_items function contains two empty lists, where the result list is empty

The functionality of the program that was not covered through automated testing, was covered through manual testing. More specifically, manual testing was needed in place where user input was required and for validating the report.txt file that was generated. 

**Note: To run the program, follow these steps:
- Run the program by using this command: `python sales_analyser.py`
- When prompted, provide the csv file name of your choice. 

The manual test cases are mentioned below:

1. Testing valid file name entered

- Input: "sample_csv" 
- Expected Output: "Please refer to 'report.txt' to see the analysis report file!"

In this use case, the user provides a valid csv file, the program analyses the csv file and outputs to a file, report.txt. The user would need to verify if report.txt is formatted correctly and displays accurate results.  

2. Testing invalid file name entered

- Input: "does_not_exist_csv"         
- Expected Output: 
<br>"This is not a valid file name. <br> Please enter a file name in the form of '___.csv':"

In this use case, the user provides a nonexistent csv file, so the program should prompt the user until the user provides a user file name. Once the user provides a valid csv file, the program analyses the csv file and outputs to a file, report.txt. 

3. Testing file with empty contents 

- Input: "empty_file.csv"                                             
- Expected Output: "Failure happened while reading file. Empty csv file provided."
                                                
In this use case, the user provides a csv file with no contents inside of it. The program would recognize this, display the error message above, indicating that an empty csv file is provided and exit the program. 

4. Testing file with header only 

- Input: "header_only.csv"                                       
- Expected Output: "Failure happened while reading file. Input file has no transaction data."

In this use case, this user provides a csv file headers and no transaction data below. The program would recognize this, display the error message above, indicating that the csv file has no transaction data and exit the program. 

5. Testing invalid entries when existing file name entered

- Input: "sample_sales_invalid_amount.csv"                                              
- Expected Output: "Failure happened while reading file. Invalid amount of sales."

In this use case, this user provides a csv file which contains an invalid value for amount (entry is string 'abc' rather than a number). The program would recognize this, display the error message above, indicating that the file has an invalid amount of sales and exit the program. 

**Note: The manual test above (#5) can also be replicated using sampe_sales_invalid_quantity.csv as the input, for which our expected output would be: "Failure happened while reading file. Invalid items sold."