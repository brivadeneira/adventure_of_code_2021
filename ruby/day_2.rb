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
end


