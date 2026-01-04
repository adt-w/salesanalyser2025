def get_unique_list(input_list):
    """This function takes in an input list and returns a new list without any duplicates."""
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def extract_year(date_string):
    """This function takes in a date string of yyyy-mm-dd, splits the string into a list 
    and  returns year extracted part from the list."""
    year = date_string.split("-")[0]
    return year

def get_common_items(list1, list2):
    """This function takes in two lists and returns a list with the common items in both."""
    items = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2 and item1 not in items:
                items.append(item1)
    return items 




