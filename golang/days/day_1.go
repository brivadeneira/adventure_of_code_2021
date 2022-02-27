package days

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

// Returns the number of measurements that increase inside three elements windows
// according to part2 of https://adventofcode.com/2021/day/1
func GetWindowSums(m []int) []int {
	var winSums []int
	for i, _ := range m {
		winSum := 0
		if i+1 == len(m) {
			winSums = append(winSums, m[i])
			break
		}
		if i+2 == len(m) {
			winSum = m[i] + m[i+1]
			winSums = append(winSums, winSum)
			continue
		}
		for _, n := range m[i : i+3] {
			winSum += n
		}
		winSums = append(winSums, winSum)
	}
	return winSums
}
