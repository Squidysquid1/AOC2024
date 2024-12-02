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
	fmt.Printf("###########DAY %s###########\n", day)
	switch day {
	case "1":
		fmt.Print("###########STAR 1###########\n\n")
		fmt.Println("Solving Star 1 Nieve approach: ", day01.SolveStar1Naive())
		utils.TimeIt("Star 1 Solution", func() { day01.SolveStar1Naive() })

		fmt.Println("Solving Star 1 faster approach: ", day01.SolveStar1()) // I thought would be way faster
		utils.TimeIt("Star 1 Solution", func() { day01.SolveStar1() })

		fmt.Print("###########STAR 2###########\n\n")
		fmt.Println("Solving Star 2 Nieve approach: ", day01.SolveStar2Naive())
		utils.TimeIt("Star 2 Solution", func() { day01.SolveStar2Naive() })

	case "2":
		fmt.Print("###########STAR 1###########\n\n")
		fmt.Println("Solving Star 1 Nieve approach: ", day02.SolveStar1Naive())
		utils.TimeIt("Star 1 Solution", func() { day02.SolveStar1Naive() })
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
