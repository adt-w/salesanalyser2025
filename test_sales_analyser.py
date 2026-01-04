from sales_analyser import SalesAnalyser
from utility import get_unique_list
import pytest

def test_read_valid_columns():

    expected_date = ['2025-01-06', '2025-01-07']
    expected_amount = [4.50, 9.00]
    expected_products = ['Espresso', 'Latte']
    expected_quantity_sold = [1, 2] 
    expected_transaction_id = ['C0001', 'C0002']
    expected_column_names = ['date', 'amount', 'product', 'count', 'transaction_id']

    sales_analyser = SalesAnalyser("sample_sales.csv")
    sales_analyser.read_data()

    assert expected_date == sales_analyser.date
    assert expected_amount == sales_analyser.amount
    assert expected_products == sales_analyser.products
    assert expected_quantity_sold == sales_analyser.quantity_sold
    assert expected_transaction_id == sales_analyser.transaction_id
    assert expected_column_names == sales_analyser.column_names

def test_read_empty_csv():
    sales_analyser = SalesAnalyser("empty_file.csv")
    with pytest.raises(ValueError):
        sales_analyser.read_data()

def test_read_header_only_csv():
    sales_analyser = SalesAnalyser("header_only.csv")
    with pytest.raises(ValueError):
        sales_analyser.read_data()

def test_read_data_invalid_amount():
    sales_analyser = SalesAnalyser("sample_sales_invalid_amount.csv")
    with pytest.raises(ValueError):
        sales_analyser.read_data()

def test_read_data_invalid_quantity():
    sales_analyser = SalesAnalyser("sample_sales_invalid_quantity.csv")
    with pytest.raises(ValueError):
        sales_analyser.read_data()

def test_get_unique_years():
    sales_analyser = SalesAnalyser("sample_sales.csv")
    sales_analyser.read_data()
    expected_result = ['2025']

    unique_years = sales_analyser.get_unique_years()

    assert unique_years == expected_result

def test_prepare_indexes():
    sales_analyser = SalesAnalyser("sample_sales3.csv")
    sales_analyser.read_data()

    expected_product_index = [[0,3], [1,2], [4]]
    expected_year_index = [[0, 1, 2, 3, 4]]

    unique_years = sales_analyser.get_unique_years()
    unique_products = get_unique_list(sales_analyser.products)
    sales_analyser.prepare_indexes(unique_products, unique_years)

    assert sales_analyser.indexes_for_product == expected_product_index
    assert sales_analyser.indexes_for_year == expected_year_index

def test_breakdown_of_product_and_year():
    sales_analyser = SalesAnalyser("sample_sales2.csv")
    sales_analyser.read_data()
    
    unique_years = sales_analyser.get_unique_years()
    unique_products = get_unique_list(sales_analyser.products)
    sales_analyser.prepare_indexes(unique_products, unique_years)
    result_list = sales_analyser.breakdown_of_product_and_year(unique_products, unique_years)

    assert len(result_list) == 7
    assert result_list[0].context == '2024'
    assert result_list[0].total_sales == 17.5
    assert result_list[0].total_quantity == 4

    assert result_list[1].context == 'Espresso'
    assert result_list[1].total_sales == 9.0
    assert result_list[1].total_quantity == 2

    assert result_list[2].context == 'Latte'
    assert result_list[2].total_sales == 8.5
    assert result_list[2].total_quantity == 2

    assert result_list[3].context == '2025'
    assert result_list[3].total_sales == 36.25
    assert result_list[3].total_quantity == 8

    assert result_list[4].context == 'Espresso'
    assert result_list[4].total_sales == 8.75
    assert result_list[4].total_quantity == 2

    assert result_list[5].context == 'Latte'
    assert result_list[5].total_sales == 17.50
    assert result_list[5].total_quantity == 4

    assert result_list[6].context == 'Flat White'
    assert result_list[6].total_sales == 10.00
    assert result_list[6].total_quantity == 2