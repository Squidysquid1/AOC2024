package day03

import (
	"bufio"
	"fmt"
	"os"
)

// Solution for star 1 first attempt
func SolveStar1Naive() int {
	// Read the input file
	file, err := os.Open("day03/input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return -1
	}
	defer file.Close()

	// Process the input file line by line
	var scanner = bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		fmt.Println(line)

	}

	return 0
}

// Solution for star 2 first attempt
func SolveStar2Naive() int {
	// Read the input file
	file, err := os.Open("day03/simpleinput.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return -1
	}
	defer file.Close()

	// Process the input file line by line
	var scanner = bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		fmt.Println(line)
	}

	return 0
}
