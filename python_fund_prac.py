import math
from math import factorial


condition = 4/2 == 2

if condition:
    result = True
else:
    result = False

assert result is True



## For loop



# TODO: Iterate over data_set and multiply each value to 2
# for elem in data_set:
#    #do so stuff

# for num in data_set:
#     number = num * 2
#     print(number)

data_set = [1,2,3,4,5]


def five_searcher(data):
    num_we_search_for = 5
    num_is_in_data_set = False
    # TODO: Implement iteration
    for num in data:
        if num == num_we_search_for:
            num_is_in_data_set = True
    return num_is_in_data_set


assert five_searcher(data_set) is True
assert 5 in data_set


str_data_set = ["daniel", "alex", "alfred", "cat"]


def string_searcher(string, data):
    str_in_data = False
    # TODO: Write iteration to search if "string" in "data"
    for _str in data:
        if string == str_in_data:
            str_in_data = True
    return str_in_data


assert string_searcher("miguel", str_data_set) is False
assert string_searcher("alex", str_data_set) is True
assert string_searcher("cat", str_data_set) is True
assert string_searcher("dog", str_data_set) is False
