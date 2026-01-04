from utility import get_unique_list, extract_year, get_common_items
from analysis_result import AnalysisResult
import os 

class SalesAnalyser: 
    def __init__(self, input_file_name):
        self._input_file_name = input_file_name
        self.date = []
        self.amount = []
        self.products = []
        self.quantity_sold = []
        self.transaction_id = []
        self.column_names = []
        
        self.indexes_for_product = []
        self.indexes_for_year = []

    def read_data(self):
        """This function populates the lists in the class, including information about quantity, date, etc."""

        infile = open(self._input_file_name, "r")
        line = infile.readline()

        # This check is done to be certain that an empty csv file would not be read and have its data split.
        if line != "":   
            line = line.strip()
            self.column_names = line.split(",")
            line = infile.readline()
            while line != "":
                line = line.strip()
                fields = line.split(",")
                self.date.append(fields[0])
                try:
                    self.amount.append(float(fields[1]))
                except ValueError as e:
                    raise ValueError(f"Invalid amount of sales.") from e
                
                self.products.append(fields[2])

                try:
                    self.quantity_sold.append(int(fields[3]))
                except ValueError as e:
                    raise ValueError(f"Invalid items sold.") from e

                self.transaction_id.append(fields[4])
                line = infile.readline()
            if len(self.date) == 0:
                raise ValueError(f"Input file has no transaction data.")
            infile.close()
        else:
            infile.close()
            raise ValueError(f"Empty csv file provided.") 
            

    def run_analysis(self):
        """This method prepares data for processing. analyses the data, 
        gets the output in terms of a list of AnalysisResult objects and 
        provides the output to a method to write the summary report in report.txt. """

        unique_products = get_unique_list(self.products)
        unique_years = self.get_unique_years()
        self.prepare_indexes(unique_products, unique_years)
        output = self.breakdown_of_product_and_year(unique_products, unique_years)
        self.write_report_to_file(output)
    
    def prepare_indexes(self, unique_products, unique_years):
        """This method takes in unique products/years and finds all locations (indices) 
        where they exist in the product and year member lists."""

        for product in unique_products:
            index_for_product = self.get_indexes_for_product(product)
            self.indexes_for_product.append(index_for_product)
    
        for year in unique_years:
            index_for_year = self.get_indexes_for_year(year)
            self.indexes_for_year.append(index_for_year)

    def breakdown_of_product_and_year(self, unique_products, unique_years):
        """This method iterates over all unique years and products, finds the commmon indexes for both, 
        calculates the total sales and quantities for each product under each year, 
        and returns a list of AnalysisResult objects."""

        output = []
        for year_index in range(len(unique_years)):
            year = unique_years[year_index]
            index_for_years = self.indexes_for_year[year_index]

            year_entry = AnalysisResult("level1", year, 0, 0)
            output.append(year_entry)

            total_amount_for_year = 0
            total_quantity_for_year = 0

            for product_index in range(len(unique_products)):
                product = unique_products[product_index]
                index_for_product = self.indexes_for_product[product_index]
                
                common_indexes = get_common_items(index_for_product, index_for_years)
                
                sum = 0
                for i in range(len(self.amount)):
                    if i in common_indexes:
                        sum = sum + self.amount[i]
                        
                        
                quantity = 0
                for i in range(len(self.amount)):
                    if i in common_indexes:
                        quantity = quantity + self.quantity_sold[i]   
                             
            
                if sum > 0:
                    total_amount_for_year = total_amount_for_year + sum 
                    total_quantity_for_year = total_quantity_for_year + quantity    
                    year_entry.total_sales = total_amount_for_year
                    year_entry.total_quantity = total_quantity_for_year
                    result = AnalysisResult("level2", product, sum, quantity)     

                    output.append(result)

        return output
            
    def write_report_to_file(self, output):
        """This method is responsible writing the report.txt file with proper formatting. 
        It gets a list of AnalysisResult objects as input."""

        outfile = open("report.txt", "w")
        message = "Here is a report generated through the Sales Analysis application for Aditya's Coffee Shop"
        outfile.write(message)
        for p in output:
            if p.level == "level1":
                msg = f"\nSummary for {p.context}: total sales = ${p.total_sales}, total quantity sold = {p.total_quantity}\n"
                outfile.write(msg)
            if p.level == "level2":
                msg = f"\t{p.context}: \n\t\ttotal sales = ${p.total_sales}, total quantity sold = {p.total_quantity}"
                outfile.write(msg)
            outfile.write('\n')
        outfile.close() 

    def get_indexes_for_product(self, product_name):
        """This function returns the indices where the unique product occurs in our self.products list."""
        indexes = []
        for i in range(len(self.products)):
            if self.products[i] == product_name:
                indexes.append(i)
        return indexes 
    
    def get_indexes_for_year(self, unique_year):
        """This function returns the indices where the unique year occurs in our self.date list."""
        indexes = []
        for i in range(len(self.date)):
            year = extract_year(self.date[i])
            if year == unique_year:
                indexes.append(i)
        return indexes 

    
    def get_unique_years(self):
        """This function populates a list with all the unique year values in the csv file provided."""

        unique_year = []
        for item in self.date:
            year_val = extract_year(item)
            if year_val not in unique_year:
                unique_year.append(year_val)
        return unique_year
    

def main():
    """This function prompts the user for a file, calls the SalesAnalyser class 
    and informs the user when the data has been processed."""

    file_name = input("Please enter a file name in the form of '___.csv': ")
    while not os.path.exists(file_name):
        print("This is not a valid file name. ")
        file_name = input("Please enter a file name in the form of '___.csv': ")

    sales_analysis = SalesAnalyser(file_name)

    try:
        sales_analysis.read_data()
        sales_analysis.run_analysis()
        print("Please refer to 'report.txt' to see the analysis report file!")
    except ValueError as e:
        print(f"Failure happened while reading file. {e}") 
    
if __name__ == "__main__":
    main()