package utils

import (
	"fmt"
	"time"
)

// an int abs function
func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

// TimeIt runs a function and measures the time it takes to execute.
func TimeIt(taskName string, fn func()) {
	start := time.Now()
	fn() // Run the function
	duration := time.Since(start)

	// Output the result
	fmt.Printf("%s took %v\n", taskName, duration)
}
