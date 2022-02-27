package days

// check the e object
func check(e error) {
	if e != nil {
		panic(e)
	}
}

// Returns the number of measurements that increase
// according to https://adventofcode.com/2021/day/1
func LargerMeasurementsCounter(m []int) int {
	p := -1
	l := 0
	for _, n := range m {
		if (p > 0) && (n > p) {
			l += 1
		}
		p = n
	}
	return l
}
