package main

import (
	"fmt"

	"github.com/adventure/days"
	"github.com/adventure/helper"
)

func main() {

	fmt.Println("Day 2")
	instructions := helper.GetStrInputFromFile("../input/day2_input.txt")
	fmt.Println("part 1: ", days.GetPositionProduct(instructions))
	fmt.Println("part 2: ", days.GetPositionProductWithAim(instructions))

}
