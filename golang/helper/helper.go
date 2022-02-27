package helper

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

// check the e object
func check(e error) {
	if e != nil {
		panic(e)
	}
}

// NotEqual tells whether a and b not contain the same elements.
// A nil argument is equivalent to an empty slice.
func NotEqual(a, b []int) bool {
	fmt.Println(a, b)
	if len(a) != len(b) {
		return true
	}
	for i, v := range a {
		if v != b[i] {
			return true
		}
	}
	return false
}

// Read a serie of integers from a given file path
func GetInputFromFile(path string) []int {
	m := []int{}
	file, err := os.Open(path)
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

	return m
}
