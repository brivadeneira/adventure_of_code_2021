from day_1 import larger_measurements_counter, get_window_sums
from utils import get_input_from_file

# day 1
# part 1

measurements_1 = get_input_from_file('../input/day1_input.txt')
print('Day 1')
print('part 1: ', larger_measurements_counter(measurements_1))

# part 2
measurements_2 = get_input_from_file('../input/day1_2_input.txt')
print('part 2: ', larger_measurements_counter(get_window_sums(measurements_2)))
print()

