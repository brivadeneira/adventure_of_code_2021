from utils import get_input_from_file


def get_position_product(instructions: list[str]) -> float:
    """
    Returns the product of horizontal position and depth
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


def get_position_product_with_aim(instructions: list[str]) -> float:
    """
    Returns the product of horizontal position and depth
    from a given list of str instructions like
    ['forward 5',
     'down 5',
     'forward 8',
     'up 3',
     'down 8',
     'forward 2']
     according to part 2 of https://adventofcode.com/2021/day/2
    :param instructions: (list of str)
    :return: (float) the result of multiply final horizontal position and depth e.g. 15 * 60
    """
    horizontal_position = 0
    depth = 0
    aim = 0

    for instruction in instructions:
        x = int(instruction.split(' ')[1])
        if 'forward' in instruction:
            horizontal_position += x
            depth += aim * x
        elif 'up' in instruction:
            aim -= x
        elif 'down' in instruction:
            aim += x
        else:
            raise ValueError('Invalid instruction')

    return horizontal_position * depth


test_instructions_data = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']


def test_day_2_part_1() -> None:
    assert get_position_product(test_instructions_data) == 10 * 15


def test_day_2_part_2() -> None:
    assert get_position_product_with_aim(test_instructions_data) == 15 * 60


if __name__ == '__main__':
    print('Day 2')
    # part 1
    instructions = get_input_from_file('../input/day2_input.txt')
    print('part 1: ', get_position_product(instructions))
    # part 2
    print('part 2: ', get_position_product_with_aim(instructions))

