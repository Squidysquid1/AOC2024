package main

import (
	"aoc2024/day01"
	"aoc2024/day02"
	"aoc2024/utils"
	"fmt"
	"os"
)

// Function to run a specific day
func runDay(day string) {
	switch day {
	case "1":
		fmt.Println("Solving Star 1 Nieve approach:")
		utils.TimeIt("Day 1 Solution", func() { day01.SolveDay1Star1Naive() })
		fmt.Println("Solving Star 2 Nieve approach:")
		utils.TimeIt("Day 1 Solution", func() { day01.SolveDay1Star2Naive() })

	case "2":
		utils.TimeIt("Day 2 Solution", func() { day02.SolveDay2() })
	default:
		fmt.Println("Invalid day:", day)
	}
}

// Function to run all days
func runAllDays() {
	days := []string{"1", "2"} // Add more days as you progress

	for _, day := range days {
		runDay(day)
	}
}

func main() {
	// Check if a specific day is provided via command line arguments
	args := os.Args[1:]
	if len(args) > 0 {
		// Run a specific day
		day := args[0]
		runDay(day)
	} else {
		// Run all days if no argument is passed
		runAllDays()
	}
}
