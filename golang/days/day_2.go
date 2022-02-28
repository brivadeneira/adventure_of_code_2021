package days

import (
	"strconv"
	"strings"
)

// Returns the product of horizontal position and depth
// from string instructions
// according to part1 of https://adventofcode.com/2021/day/2
func GetPositionProduct(instructions []string) int {
	hPosition, depth := 0, 0
	for _, instruction := range instructions {
		xStr := strings.Split(instruction, " ")[1]
		x, _ := strconv.Atoi(xStr)

		if strings.Contains(instruction, "forward") {
			hPosition += x
		} else {
			if strings.Contains(instruction, "up") {
				depth -= x
			} else {
				depth += x
			}
		}
	}
	return hPosition * depth
}
