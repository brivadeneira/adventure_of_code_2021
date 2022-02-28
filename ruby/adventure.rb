require_relative "day_1.rb"
require_relative "day_2.rb"
require_relative "utils.rb"

utils = Utils

# day 1

puts "Day one"
measurements = Utils.get_input_from_file("../input/day1_input.txt", true)
day_one = DayOne
puts "part 1: ", day_one.larger_measurements_counter(measurements)

measurements_2 = Utils.get_input_from_file("../input/day1_2_input.txt", true)
window_measurement = day_one.get_window_sums(measurements_2)
puts "part 2: ", day_one.larger_measurements_counter(window_measurement)

# day 2

puts "Day two"
day_two = DayTwo
instructions = Utils.get_input_from_file("../input/day2_input.txt", false)
puts "part 1: ", day_two.get_position_product(instructions)