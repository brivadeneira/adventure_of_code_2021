package days

import (
	"testing"
)

func TestGetPositionProduct(t *testing.T) {
	expected := 10 * 15

	instructions := []string{"forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"}
	got := GetPositionProduct(instructions)

	if got != expected {
		t.Errorf("Expected: %v, got: %v", expected, got)
	}
}
