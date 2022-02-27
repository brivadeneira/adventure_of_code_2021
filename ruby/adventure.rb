require_relative "day_1.rb"

# day 1
file = File.open("../input/day1_input.txt")
str_numbers = file.readlines.map(&:chomp)

measurements = []
str_numbers.each {|str_num|
    measurements.append(str_num.to_i)
}
puts "Day one"
day_one = DayOne
puts day_one.larger_measurements_counter(measurements)