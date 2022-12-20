package main

import (
	"fmt"
)

func main() {
	lst := []int{0, 1, 1, 0, 1, 0, 0, 0, 1}
	fmt.Println(day_607(lst))
}

func day_607(lst []int) int {
	indexes := []int{}
	distance := 0

	for index, item := range lst {
		if item == 1 {
			indexes = append(indexes, index)
		}
	}
	for i := 0; i < (len(indexes) -1); i++ {
		if indexes[i + 1] - indexes[i] > 1 {
			distance += indexes[i + 1] - (indexes[i] + 1)
			indexes[i + 1] = indexes[i] + 1
		}
	}
	return distance
}