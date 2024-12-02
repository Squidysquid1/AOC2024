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

// TimeIt runs a function and measures the average time it takes to execute.
func TimeIt(taskName string, fn func()) {
	var totalDuration time.Duration

	runs := 10
	for i := 0; i < runs; i++ {
		start := time.Now()
		fn() // Run the function
		duration := time.Since(start)
		totalDuration += duration
	}

	averageDuration := totalDuration / time.Duration(runs)

	// Output the result
	fmt.Printf("%s took %v\n\n", taskName, averageDuration)
}
