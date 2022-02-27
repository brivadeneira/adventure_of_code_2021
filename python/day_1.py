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
