package main

import (
	"fmt"
	"strings"
)

func main() {

}

func day_619(lst []string, word string) bool {
	cond := false
	v := strings.SplitAfter(word, "")
	i, j := 0, 0
	for _, val := range lst {
		for _, item := range val {
			if item == v[0] {
				soln :=parse([i, j], lst, v)
			}
			j += 1
		}
		i += 1
		j = 0
	}
	// return cond
}

func parse(lst []int, listt []string, v []string, cur int) bool {
	if i < (len(listt) - 1) && j {

	}

	if listt[i][j+1] == v[cur] {

	} else if listt[i][j-1] == v[cur] {

	} else if
	return cond
}