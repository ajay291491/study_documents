#!/usr/bin/python
#
#
def join_a_list(list_name):
    joined_list = "-".join(list_name)
    return joined_list

fruit_basket = ['apple', 'vanila', 'strawberry', 'cherry', 'plum']
print join_a_list(fruit_basket)
