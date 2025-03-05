#!/bin/bash

# Check if an argument is not provided
if [ -z "$1" ]; then
    echo "Usage: $0 <number>"
    exit 1
fi

# Compile
javac FizzBuzz.java

# Run the Java program with the provided argument
java FizzBuzz "$1"

# delete auto-generated .class file that Intellij made
rm FizzBuzz.class