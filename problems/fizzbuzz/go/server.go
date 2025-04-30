package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strconv"
)

func generateWordsHandler(w http.ResponseWriter, r *http.Request) {
	nStr := r.URL.Query().Get("n")
	n, err := strconv.Atoi(nStr)
	if err != nil || n <= 0 {
		http.Error(w, "Invalid n", http.StatusBadRequest)
		return
	}
	words := generateWords(n)
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(words)
}

func main() {
	http.HandleFunc("/generate", generateWordsHandler)
	fmt.Println("Server listening on http://localhost:8080")
	http.ListenAndServe(":8080", nil)
}
