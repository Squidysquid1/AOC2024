package day02

import (
	"fmt"
	"os"
)

// Solution for star 1 first attempt
func SolveStar1Naive() int {
	// Read the input file
	file, err := os.Open("day02/input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return -1
	}
	defer file.Close()

	/*// Process the input file line by line
	var numbers []int
	var scanner = bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		// Parse each line to an integer and store it in the numbers slice
		num, err := strconv.Atoi(strings.TrimSpace(line))
		if err != nil {
			fmt.Println("Error parsing number:", err)
			return
		}
		numbers = append(numbers, num)
	}

	// Solve the puzzle (example: sum of numbers)
	sum := 0
	for _, num := range numbers {
		sum += num
	}

	*/
	return -1
}

// Solution for star 2 first attempt
func SolveStar2Naive() int {
	return -1
}
