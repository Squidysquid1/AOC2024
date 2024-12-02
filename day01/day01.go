package day01

import (
	"aoc2024/utils"
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

// Solution for star 1 first attempt
func SolveStar1Naive() int {
	// Read the input file
	file, err := os.Open("day01/input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return -1
	}
	defer file.Close()

	//Process the input file line by line
	var leftNum []int
	var rightNum []int
	var scanner = bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()

		numbers := strings.Fields(line)

		leftNumToAppend, err1 := strconv.Atoi(numbers[0])
		leftNum = append(leftNum, leftNumToAppend)

		rightNumToAppend, err2 := strconv.Atoi(numbers[1])
		rightNum = append(rightNum, rightNumToAppend)

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

	return sum
}

// Solution for star 2 first attempt
func SolveStar2Naive() int {
	// Read the input file
	file, err := os.Open("day01/input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return -1
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

	return sum
}

// revised solution that uses heap. Look into why it is so slow. Might have to implement heap myself
func SolveStar1() int {
	// Read the input file
	file, err := os.Open("day01/input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return -1
	}
	defer file.Close()

	lHeap := &utils.IntHeap{}
	heap.Init(lHeap)

	rHeap := &utils.IntHeap{}
	heap.Init(rHeap)

	var scanner = bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()

		numbers := strings.Fields(line)

		leftNumToAppend, err1 := strconv.Atoi(numbers[0])
		heap.Push(lHeap, leftNumToAppend)

		rightNumToAppend, err2 := strconv.Atoi(numbers[1])
		heap.Push(rHeap, rightNumToAppend)

		if err1 != nil {
			fmt.Println("Error convering numbers:", err1)
		}
		if err2 != nil {
			fmt.Println("Error convering numbers:", err2)
		}
	}

	sum := 0
	for lHeap.Len() > 0 {
		sum += utils.Abs(heap.Pop(rHeap).(int) - heap.Pop(lHeap).(int))
	}

	return sum
}
