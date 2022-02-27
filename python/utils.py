def get_input_from_file(file_path: str) -> list[int]:
    """
    Returns a list according to an input file
    :param file_path: (str) input file data
    :return: (list of ints) with input data
    """
    with open(file_path) as f:
        input = [int(line) for line in f.readlines()]
        return input