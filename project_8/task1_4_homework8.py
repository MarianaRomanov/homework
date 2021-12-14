from task1_1_3_homework8 import filter_list_by_type


def remove_not_alpha_from_str(string):
    return ''.join(char for char in string if char.isalpha())


def remove_not_alpha_from_list_elements(list_in) -> list:
    return [remove_not_alpha_from_str(i) for i in list_in]


if __name__ == '__main__':
    print(remove_not_alpha_from_list_elements(
          filter_list_by_type([3, 'tr% 5r', 65, 78, '8ty/7', {'name': 'test'}, 1.23, 'ytr_6g'], [str])))
