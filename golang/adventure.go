package main

import (
	"fmt"

	"github.com/adventure/days"
	"github.com/adventure/helper"
)

func main() {
	fmt.Println("Day 1")
	m := helper.GetIntInputFromFile("../input/day1_input.txt")

	c := days.LargerMeasurementsCounter(m)
	fmt.Println("part 1: ", c)

	m2 := helper.GetIntInputFromFile("../input/day1_2_input.txt")
	w := days.GetWindowSums(m2)
	c2 := days.LargerMeasurementsCounter(w)

	fmt.Println("part 2: ", c2)

	fmt.Println("Day 2")
	instructions := helper.GetStrInputFromFile("../input/day2_input.txt")
	fmt.Println("part 1: ", days.GetPositionProduct(instructions))

}
