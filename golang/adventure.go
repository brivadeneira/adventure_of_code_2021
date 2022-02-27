package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"

	"github.com/adventure/days"
)

func main() {
	fmt.Println("Day 1")

	m := []int{}
	file, err := os.Open("../input/day1_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		s := scanner.Text()
		n, err := strconv.Atoi(s)

		if err != nil {
			// handle error
			fmt.Println(err)
			os.Exit(2)
		}

		m = append(m, n)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	counter := days.LargerMeasurementsCounter(m)
	fmt.Println(counter)
}
