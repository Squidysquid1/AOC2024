package day01

import (
	"aoc2024/utils"
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

// Solution for Day 1
func SolveDay1Star1Naive() {
	// Read the input file
	file, err := os.Open("day01/input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	//Process the input file line by line
	var leftNum []int
	var rightNum []int
	var scanner = bufio.NewScanner(file)
	i := 0
	for scanner.Scan() {
		line := scanner.Text()

		numbers := strings.Fields(line)

		leftNumToAppend, err1 := strconv.Atoi(numbers[0])
		leftNum = append(leftNum, leftNumToAppend)

		rightNumToAppend, err2 := strconv.Atoi(numbers[1])
		rightNum = append(rightNum, rightNumToAppend)

		i++

		if err1 != nil {
			fmt.Println("Error convering numbers:", err1)
		}
		if err2 != nil {
			fmt.Println("Error convering numbers:", err2)
		}
	}

	// Solve the puzzle
	slices.Sort(leftNum)
	slices.Sort(rightNum)

	sum := 0
	for i := 0; i < len(leftNum); i++ {
		sum += utils.Abs(rightNum[i] - leftNum[i])
	}

	fmt.Println("Solution:", sum)
}

func SolveDay1Star2Naive() {
	// Read the input file
	file, err := os.Open("day01/input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	//Process the input file line by line
	var leftNum []int
	var rightNum []int
	var scanner = bufio.NewScanner(file)
	i := 0
	for scanner.Scan() {
		line := scanner.Text()

		numbers := strings.Fields(line)

		leftNumToAppend, err1 := strconv.Atoi(numbers[0])
		leftNum = append(leftNum, leftNumToAppend)

		rightNumToAppend, err2 := strconv.Atoi(numbers[1])
		rightNum = append(rightNum, rightNumToAppend)

		i++

		if err1 != nil {
			fmt.Println("Error convering numbers:", err1)
		}
		if err2 != nil {
			fmt.Println("Error convering numbers:", err2)
		}
	}

	numberCnt := make(map[int]int)
	for i := 0; i < len(rightNum); i++ {
		numberCnt[rightNum[i]]++
	}

	sum := 0
	for i := 0; i < len(leftNum); i++ {
		sum += leftNum[i] * numberCnt[leftNum[i]]
	}

	fmt.Println("Solution:", sum)
}
