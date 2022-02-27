from day_1 import get_window_sums, larger_measurements_counter
from day_2 import get_position_product
from utils import get_input_from_file

# day 1
print('Day 1')

# part 1
measurements_1 = get_input_from_file('../input/day1_input.txt', True)
print('part 1: ', larger_measurements_counter(measurements_1))

# part 2
measurements_2 = get_input_from_file('../input/day1_2_input.txt', True)
print('part 2: ', larger_measurements_counter(get_window_sums(measurements_2)))
print()

# day 2
print('Day 2')
# part 1
instructions = get_input_from_file('../input/day2_input.txt')
print('part 1: ', get_position_product(instructions))


