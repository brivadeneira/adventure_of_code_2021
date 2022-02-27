def get_position_product(instructions: list[str]) -> float:
    """
    Returns the product of horizontal position an depth
    from a given list of str instructions like
    ['forward 5',
     'down 5',
     'forward 8',
     'up 3',
     'down 8',
     'forward 2']
     according to https://adventofcode.com/2021/day/2
    :param instructions: (list of str)
    :return: (float) the result of multiply final horizontal position and depth e.g. 10 * 15
    """
    horizontal_position = 0
    depth = 0

    for instruction in instructions:
        x = int(instruction.split(' ')[1])
        if 'forward' in instruction:
            horizontal_position += x
        elif 'up' in instruction:
            depth -= x
        else:
            depth += x

    return horizontal_position * depth


def test_day_2_part_1() -> None:
    test_instructions_data = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
    assert get_position_product(test_instructions_data) == 10 * 15


