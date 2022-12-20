package main

import (
	"fmt"
	"strings"
)

func main() {


	fmt.Println(50 - 52)


	// variable
	var myAge int =  333
	// constants
	const myName string = "Damilare"
	fmt.Println("Hello")
	// for place holders
	fmt.Printf("I am %v", myAge)
	fmt.Println("")
	fmt.Printf("My name is %v", myName)
	fmt.Println("")

	var myHeight int
	myHeight = 168
	// alternate variable syntax
	// doesn't work for constants
	myWeight := 67


	fmt.Printf("I am %v tall", myHeight)
	fmt.Println("")
	fmt.Printf("I weigh %v", myWeight)
	fmt.Println("")
	fmt.Printf("It is a %T data type", myHeight)
	fmt.Println("")

	// a pointer shows us the memory address of a value assigned variable
	// - a variable is assigned a value `var v int = 2`
	// - v points to 2 in memory by searching with the memory address
	// - &v gives us the memory address itself

	fmt.Println(myAge)
	fmt.Println(&myAge)

	var firstUserInput uint
	// assign the value to the pointer
	fmt.Scan(&firstUserInput)
	fmt.Println(firstUserInput)

	// array
	// it has a fixed size, type, elements
	// empty array
	var lst [50]string
	// not empty
	var anoLst = [50]uint{1,2,3}
	// edit array elements using index
	lst[0] = "one"

	fmt.Printf("The list %v\n", lst)
	fmt.Printf("The other list length %v\n", len(anoLst))
	fmt.Printf("A list of type %T\n", lst)

	// slice
	// an abstraction of an array
	// you dont need to define a size
	var sliceHere []string	// var anotherSlice = []uint{}
	slice2 := []string{"ade"}

	fmt.Printf("The slice %v\n", sliceHere)
	fmt.Printf("The slice of length %v\n", len(slice2))
	fmt.Printf("A slice of type %T\n", slice2)
	// to add to slice
	sliceHere = append(sliceHere, "first")

	//firstNames := []string{}
	for index, item := range anoLst {
		fmt.Println(index, " ", item)
	}

	thisString := "John Doe"
	// to split a string
	names := strings.Fields(thisString)
	firstName := names[0]
	fmt.Printf("The name is %v", firstName)

	// underscores are used to identify unused variables
	// especially where we have to declare them
	for _, item := range anoLst {
		fmt.Println(" ", item)
		break	// and continue
	}

	// conditional statement
	// if condition {
	// } else {
	// }
	nameIsPay := firstName == "pay"
	if nameIsPay {		// if firstName == "pay" {}
		fmt.Println("Its the name")
	} else {
		fmt.Println("Its not the name")
	}



}
