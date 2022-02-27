##
# This class has general methods needed for solve adventure of code 2011 problems.

class Utils
    def self.get_input_from_file(file_path)
        ##
        # Return an array of ints from a given txt file path
        file = File.open("../input/day1_input.txt")
        str_numbers = file.readlines.map(&:chomp)

        array = []
        str_numbers.each {|str_num|
            array.append(str_num.to_i)
        }
        return array
    end
end