require "test/unit"
require_relative "day_1.rb"

class TestDayOne < Test::Unit::TestCase
    def test_day_one
        test_measurements_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        assert_equal(7, DayOne.larger_measurements_counter(test_measurements_data))

        expected = [607, 618, 618, 617, 647, 716, 769, 792, 523, 263]
        assert_equal(expected, DayOne.get_window_sums(test_measurements_data))
    end
end