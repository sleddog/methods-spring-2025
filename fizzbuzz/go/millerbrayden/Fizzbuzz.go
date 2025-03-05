package main

import (
	"fmt"
	"os"
	"strconv"
)

func printWords(n int) {
	for i := 1; i <= n; i++ {
		switch {
		case i%15 == 0:
			fmt.Println("BobCat")
		case i%3 == 0:
			fmt.Println("Bob")
		case i%5 == 0:
			fmt.Println("Cat")
		default:
			fmt.Println(i)
		}
	}
}

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Usage: ./fizzbuzz <number>")
		return
	}
	n, err := strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Println(err)
		return
	}
	printWords(n)
}
