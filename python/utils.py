from typing import Union

InputType = list[Union[str, int]]


def get_input_from_file(file_path: str, to_int: bool = False) -> InputType:
    """
    Returns a list according to an input file
    :param to_int: (bool) convert to int each line of input if True
    :param file_path: (str) input file data
    :return: (list) with input data
    """
    with open(file_path) as f:
        if to_int:
            return [int(line) for line in f.readlines()]
        else:
            return [line.replace('\n', '') for line in f.readlines()]
