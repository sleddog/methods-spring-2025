package main

import (
	"bytes"
	"fmt"
	"os"
	"strings"
	"strconv"
	"testing"
)







func getFizzbuzzOutput(n int) []string {
	original_stdout := os.Stdout             // Save the original stdout
	r, w, _ := os.Pipe()                     // Create a pipe to capture output
	os.Stdout = w                            // Redirect stdout to the pipe
	os.Args = []string{"Fizzbuzz", fmt.Sprintf("%d", n)} 
	main()                                   // Call the function that prints to stdout
	w.Close()                                // Close the write end of the pipe
	os.Stdout = original_stdout              // Restore original stdout
	var pipe_buffer bytes.Buffer
	_, _ = pipe_buffer.ReadFrom(r)           // Read captured output
	captured_output := strings.Split(pipe_buffer.String(), "\n")      // convert the captured output into a slice of strings
	return captured_output           
}








func TestJustNumber(t *testing.T) {
	output := getFizzbuzzOutput(2)
	if output[1] != strconv.Itoa(2) {
		t.Errorf("Expected 2, Got '%s'", output[1])
	}
}


func TestBob(t *testing.T) {
	output := getFizzbuzzOutput(3)
        if output[2] != "Bob" {
                t.Errorf("Expected Bob, Got '%s'", output[2])
        }	
}


func TestCat(t *testing.T) {
	output := getFizzbuzzOutput(5)
        if output[4] != "Cat" {
                t.Errorf("Expected Cat, Got '%s'", output[4])
        }
}

func TestBobcat(t *testing.T) {
	output := getFizzbuzzOutput(15)
        if output[14] != "BobCat" {
                t.Errorf("Expected BobCat, Got '%s'", output[14])
        }
}
