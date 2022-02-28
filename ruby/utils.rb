##
# This class has general methods needed for solve adventure of code 2011 problems.

class Utils
    def self.get_input_from_file(file_path, to_int)
        ##
        # Return an array of ints or str from a given txt file path
        file = File.open(file_path)
        items = file.readlines.map(&:chomp)

        array = []

        if to_int
            items.each {|str_num|
                array.append(str_num.to_i)
            }
        else
            items.each {|str|
                array.append(str)
            }
        end
        return array
    end
end