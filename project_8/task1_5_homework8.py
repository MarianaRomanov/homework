from project_8.task1_4_homework8 import remove_not_alpha_from_str


li = {'name': 'Test', 'surname': 'Black_1', 'age': 21, 'position': 'QA',
      'address': 'Ukraine, Kyiv, Main str, 23',
      'skills': ['Automation', 'Python', 'Git']}


def generate_dict_with_type_in_values(new_li) -> dict:
    return {key: type(value) for key, value in new_li.items()}


def remove_not_alpha_from_dict_values(new_li) -> dict:
    return {key: remove_not_alpha_from_str(value).lower() for key, value in new_li.items() if type(value) is str}


if __name__ == '__main__':
    print(generate_dict_with_type_in_values(li))
    print(remove_not_alpha_from_dict_values(li))
