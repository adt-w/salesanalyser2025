from utility import get_unique_list, extract_year, get_common_items
import pytest

def test_get_unique_list_with_duplicates():

    initial_list = ["apple", "orange", "grapes", "apple", "orange"]
    expected_list = ["apple", "orange", "grapes"]

    unique_list = get_unique_list(initial_list)
    
    assert unique_list == expected_list

def test_get_unique_list_with_empty_list():

    initial_list = []
    expected_list = []

    unique_list = get_unique_list(initial_list)
    
    assert unique_list == expected_list

def test_get_valid_extraction_of_year():
    expected_year = "2025"

    year_val = extract_year("2025-01-06")

    assert year_val == expected_year

def test_valid_common_items():
    list1 = [1,2,3,4]
    list2 = [4,5,6,7,8]
    expected_result = [4]

    result = get_common_items(list1, list2)

    assert result == expected_result

def test_no_common_items():
    list1 = [1,2,3,4]
    list2 = [5,6,7,8]
    expected_result = []

    result = get_common_items(list1, list2)

    assert result == expected_result

def test_common_items_with_empty_list_single():
    list1 = []
    list2 = [2,3,4]
    expected_result = []

    result = get_common_items(list1, list2)

    assert result == expected_result

def test_common_items_with_empty_list_both():
    list1 = []
    list2 = []
    expected_result = []

    result = get_common_items(list1, list2)

    assert result == expected_result