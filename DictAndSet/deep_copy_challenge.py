from contents import recipes


def my_deepcopy(d: dict) -> dict:
    """
    Copy a dictionary, creating copies of the `list` or `dict` values.

    The function will crash with an AttributeError if the values are not
    lists or dictionaries

    :param d: The dictionary to copy.
    :return: A copy of `d`, with the values being copies of the original values.
    """
    my_copy = {}
    for key, value in d.items():
        new_value = value.copy()
        my_copy[key] = new_value

    return my_copy


recipes_copy = my_deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])
