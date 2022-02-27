from day_1 import larger_measurements_counter

# day 1
with open('../input/day1_input.txt') as f:
    measurements = [int(line) for line in f.readlines()]

print('Day 1')
print(larger_measurements_counter(measurements))