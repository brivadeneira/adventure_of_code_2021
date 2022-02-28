require_relative "utils.rb"

##
# This class has the method needed for the day one of adventure of code 2011.

class DayOne
    def self.larger_measurements_counter(measurements)
        ##
        # Returns the number of measurements that increase
        # according to https://adventofcode.com/2021/day/1
        counter = 0
        previous = nil

        measurements.each { |num|
            if previous and num > previous
                counter += 1
            end
            previous = num
        }

        return counter
    end

    def self.get_window_sums(measurements)
        ##
        # Returns a list with window sums
        # accordint to part 2 of https://adventofcode.com/2021/day/1
        win_sums = []
        measurements.each_with_index { | _, i |
            win_sum = 0
            measurements[i,3].each { |n|
                win_sum += n
            }
            win_sums.append(win_sum)
        }
        return win_sums
    end
end


utils = Utils

# day 1

puts "Day one"
measurements = Utils.get_input_from_file("../input/day1_input.txt", true)
day_one = DayOne
puts "part 1: ", day_one.larger_measurements_counter(measurements)

measurements_2 = Utils.get_input_from_file("../input/day1_2_input.txt", true)
window_measurement = day_one.get_window_sums(measurements_2)
puts "part 2: ", day_one.larger_measurements_counter(window_measurement)
