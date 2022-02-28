require_relative "utils.rb"

##
# This class has the method needed for the day two of adventure of code 2011.

class DayTwo
    def self.get_position_product(instructions)
        ##
        # Returns the product of horizontal position an depth
        # from a given list of str instructions like
        # ['forward 5',
        #  'down 5',
        #  'forward 8',
        #  'up 3',
        #  'down 8',
        #  'forward 2']
        #  according to https://adventofcode.com/2021/day/2

        horizontal_position = 0
        depth = 0

        instructions.each { |instruction|
            x = instruction.split(" ", -1)[1].to_i
            if instruction.include? "forward"
                horizontal_position += x              
            elsif instruction.include? "up"
                depth -= x
            else
                depth += x
            end
        }

        return horizontal_position * depth
    end

    def self.get_position_product_with_aim(instructions)
        ##
        # Returns the product of horizontal position an depth
        # from a given list of str instructions like
        # ['forward 5',
        #  'down 5',
        #  'forward 8',
        #  'up 3',
        #  'down 8',
        #  'forward 2']
        #  according to part 2 of https://adventofcode.com/2021/day/2

        horizontal_position = 0
        depth = 0
        aim = 0

        instructions.each { |instruction|
            x = instruction.split(" ", -1)[1].to_i
            if instruction.include? "forward"
                horizontal_position += x
                depth += aim * x           
            elsif instruction.include? "up"
                aim -= x
            else
                aim += x
            end
        }

        return horizontal_position * depth
    end
end

utils = Utils

puts "Day two"
day_two = DayTwo
instructions = Utils.get_input_from_file("../input/day2_input.txt", false)
print "part 1: ", day_two.get_position_product(instructions)
puts ""
print "part 2: ", day_two.get_position_product_with_aim(instructions)
puts ""

