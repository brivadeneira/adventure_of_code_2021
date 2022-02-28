from collections import Counter
from utils import get_input_from_file


def calculate_power_consumption(binary_report: list[str]) -> int:
    """
    Return the power consumption of a submarine
    from a given binary report
    according to https://adventofcode.com/2021/day/3
    :param binary_report: (list of str) with reports
    :return: (int) power consumption
    """
    bin_counter = []
    bin_len = len(binary_report[0])

    for i in range(bin_len):
        c = Counter([b[i] for b in binary_report]).most_common()
        bin_counter.append(c)

    gamma_rate = ''.join([c[0][0] for c in bin_counter])
    epsilon_rate = ''.join([c[1][0] for c in bin_counter])

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def test_day_3part_1() -> None:
    test_binary_report = ['00100', '11110', '10110', '10111',
                          '10101', '01111', '00111', '11100',
                          '10000', '11001', '00010', '01010']
    assert calculate_power_consumption(test_binary_report) == 22 * 9


if __name__ == '__main__':
    print('Day 3')
    # part 1
    binary_report = get_input_from_file('../input/day3_input.txt')
    print('part 1: ', calculate_power_consumption(binary_report))
