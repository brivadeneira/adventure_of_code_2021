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
end


