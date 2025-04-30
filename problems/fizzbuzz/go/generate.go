package main

import "strconv"

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