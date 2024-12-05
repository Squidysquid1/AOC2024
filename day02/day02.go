package day02

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
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

	safe := 0
	// Process the input file line by line
	var scanner = bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()

		numbers := strings.Split(line, " ")

		if checkIfSafe(numbers) {
			safe++
		}

	}

	return safe
}

// Solution for star 2 first attempt
func SolveStar2Naive() int {
	// Read the input file
	file, err := os.Open("day02/simpleinput.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return -1
	}
	defer file.Close()

	safe := 0
	// Process the input file line by line
	var scanner = bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()

		numbers := strings.Split(line, " ")

		if checkIfSafeWithOneBadLevel(numbers) {
			safe++
		}

	}

	return safe
}

func checkIfSafe(nums []string) bool {
	previous, _ := strconv.Atoi(nums[0])
	isAccending := true
	for i := 1; i < len(nums); i++ {
		curNum, _ := strconv.Atoi(nums[i])

		difference := curNum - previous

		if i == 1 {
			// difference is positive it is decending
			isAccending = difference > 0
		}

		if isAccending && difference <= 0 {
			// if accending and next number is not
			return false
		} else if !isAccending && difference >= 0 {
			// if decending and next number is not
			return false
		} else if utils.Abs(difference) > 3 {
			// if the next difference is 2 big
			return false
		}

		previous = curNum
	}

	return true
}

// Give up and brute force... so bad will revisit idk
func checkIfSafeWithOneBadLevel(nums []string) bool {
	if checkIfSafe(nums) {
		return true
	}

	for index := range nums {
		newSlice := append(nums[:index], nums[(index+1):]...)
		fmt.Println(newSlice)
		if checkIfSafe(newSlice) {
			return true
		}
	}
	return false
}
