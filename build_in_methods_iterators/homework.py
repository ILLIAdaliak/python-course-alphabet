from typing import List, Dict, Union, Generator
import string
import random
import functools

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    """
    Make all `names` field in list of students to start from upper letter

    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
        >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]
    """
    for member in data:
        if member.get('name') is not None:
            member['name'] = member['name'].capitalize()
    return data



def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    """given_data
    Remove from dictionaries given key value

    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]

    """
    return [{k: v for k, v in i.items() if k not in redundant_keys} for i in data]


def task_3_find_item_via_value(data: DT, value) -> DT:
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """
    return [d for d in data if value in d.values()]



def task_4_min_value_integers(data: List[int]) -> int:
    """
    Find and return minimum value from list
    """
    if len(data) > 0:
        return min(data)


def task_5_min_value_strings(data: List[Union[str, int]]) -> str:
    """
    Find the longest string
    """
    if len(data) > 0:

        return str(min(data, key=lambda x: len(str(x))))


def task_6_min_value_list_of_dicts(data: DT, key: str) -> ST:
    """
    Find minimum value by given key
    Returns:

    """
    filter = [item for item in data if item.get("age", None)]

    return min(filter, key=lambda x: x.get(key))

def task_7_max_value_list_of_lists(data: List[List[int]]) -> int:
    """
    Find max value from list of lists
    """
    max_list = max(map(lambda x: x, data))
    return max(map(lambda x: x, max_list))


def task_8_sum_of_ints(data: List[int]) -> int:
    """
    Find sum of all items in given list
    """

    return sum(map(lambda x: x, data))


def task_9_sum_characters_positions(text: str) -> int:
    """
    Please read first about ascii table.
    https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
    You need to calculate sum of decimal value of each symbol in text

    Examples:
        task_9_sum_characters_positions("A")
        >>> 65
        task_9_sum_characters_positions("hello")
        >>> 532

    """



    return sum([ord(x) for x in text])


def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:
    """
    Return generator of simple numbers
    Stop then iteration if returned value is more than 200
    Examples:
        a = task_10_generator_of_simple_numbers()
        next(a)
        >>> 2
        next(a)
        >>> 3"""

    for num in range(2,200):
     if all(num%i!=0 for i in range(2,num)):
       yield num





def task_11_create_list_of_random_characters() -> List[str]:
    """
    Create list of 20 elements where each element is random letter from latin alphabet

    """


    return [random.choice(string.ascii_letters.lower()) for _ in range(20)]
