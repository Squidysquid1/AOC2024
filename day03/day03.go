package day03

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
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

	re := regexp.MustCompile(`mul\(\d{1,3},\d{1,3}\)`)
	var toMultiply []string
	// Process the input file line by line
	var scanner = bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		regExMatches := re.FindAllString(line, -1)
		toMultiply = append(toMultiply, regExMatches...)

	}
	//fmt.Println(toMultiply)

	sum := 0
	for _, element := range toMultiply {
		nums := strings.Split(element[4:len(element)-1], ",")
		num1, _ := strconv.Atoi(nums[0])
		num2, _ := strconv.Atoi(nums[1])
		sum += num1 * num2
	}

	return sum
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
