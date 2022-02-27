package days

import "testing"

func TestLargerMeasurementsCounter(t *testing.T) {
	expected := 7

	m := []int{199, 200, 208, 210, 200, 207, 240, 269, 260, 263}
	got := LargerMeasurementsCounter(m)

	if got != expected {
		t.Errorf("Expected: %v, got: %v", expected, got)
	}
}
