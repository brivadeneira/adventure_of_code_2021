from utils import get_input_from_file


def larger_measurements_counter(measurements: list[int]) -> int:
    """
    Returns the number of measurements that increase
    according to https://adventofcode.com/2021/day/1
    :param measurements: (list of int) with measurements
    :return: (int) the number og measurements that increase
    """
    larger_measurements = 0
    previous = 0

    for num in measurements:
        if previous and num > previous:
            larger_measurements += 1
        previous = num

    return larger_measurements


def get_window_sums(measurements: list[int]) -> list[int]:
    """
    Returns a list with window sums
    accordint to part 2 of https://adventofcode.com/2021/day/1
    :param measurements: (list of int) with measurements
    :return: (list of int) window sums
    """
    win_sums = []

    for i, _ in enumerate(measurements):
        win_sum = sum(measurements[i:i + 3])
        win_sums.append(win_sum)

    return win_sums


def test_day_1_part_1() -> None:
    test_measurements_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert larger_measurements_counter(test_measurements_data) == 7


def test_day_1_part_2() -> None:
    test_measurements_data_2 = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert (get_window_sums(test_measurements_data_2)) == [607, 618, 618, 617, 647, 716, 769, 792, 523, 263]


if __name__ == '__main__':
    print('Day 1')

    # part 1
    measurements_1 = get_input_from_file('../input/day1_input.txt', True)
    print('part 1: ', larger_measurements_counter(measurements_1))

    # part 2
    measurements_2 = get_input_from_file('../input/day1_2_input.txt', True)
    print('part 2: ', larger_measurements_counter(get_window_sums(measurements_2)))
