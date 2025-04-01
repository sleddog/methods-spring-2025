package main

import (
	"fmt"
	"os"
	"strconv"
)

func generateWords(n int) []string {
	var result []string
	for i := 1; i <= n; i++ {
		switch {
		case i%15 == 0:
			result = append(result, "BobCat")
		case i%3 == 0:
			result = append(result, "Bob")
		case i%5 == 0:
			result = append(result, "Cat")
		default:
			result = append(result, strconv.Itoa(i))
		}
	}
	return result
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

	words := generateWords(n)
	for _, word := range words {
		fmt.Println(word)
	}
}
