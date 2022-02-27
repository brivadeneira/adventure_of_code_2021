package days

import (
	"github.com/adventure/helper"
	"testing"
)

func TestLargerMeasurementsCounter(t *testing.T) {
	expected := 7

	m := []int{199, 200, 208, 210, 200, 207, 240, 269, 260, 263}
	got := LargerMeasurementsCounter(m)

	if got != expected {
		t.Errorf("Expected: %v, got: %v", expected, got)
	}
}

func TestWindowSums(t *testing.T) {
	expected := []int{607, 618, 618, 617, 647, 716, 769, 792, 523, 263}

	m := []int{199, 200, 208, 210, 200, 207, 240, 269, 260, 263}
	got := GetWindowSums(m)

	if helper.NotEqual(got, expected) {
		t.Errorf("Expected: %v, got: %v", expected, got)
	}
}
