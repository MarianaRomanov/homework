def generate_list_of_two_to_the_power_n():
    return [pow(2, n) for n in range(20)]


def generate_list_of_remainder_of_division_on_three(li_in):
    return [i % 3 for i in li_in]


def filter_list_by_type(list_in, type_in) -> list:
    return [i for i in list_in if type(i) in type_in]


if __name__ == '__main__':
    print(generate_list_of_two_to_the_power_n())
    print(generate_list_of_remainder_of_division_on_three([2, 4, 54, 22, 54, 7676, 764, 77798, 43, 23, 657]))
    print(filter_list_by_type([3, 'trr', 65, 78, '87', {'name': 'test', 'age': 9}, 1.23, 10], [int, float]))
