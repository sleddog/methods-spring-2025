#!/bin/bash

# If the --test flag is provided, run tests.
if [ "$1" == "--test" ]; then
    # Ensure the JUnit 5 standalone jar is present in the current directory.
    JUNIT_JAR="junit-platform-console-standalone-1.12.1.jar"

    if [ ! -f "$JUNIT_JAR" ]; then
        echo "Error: $JUNIT_JAR not found. Please download it and place it in the current directory."
        exit 1
    fi

    # Compile production and test classes with the JUnit jar in the classpath.
    javac -cp .:"$JUNIT_JAR" FizzBuzz.java FizzBuzzTest.java

    # Run the tests using the JUnit 5 Console Launcher.
    java -jar "$JUNIT_JAR" execute --class-path . --scan-class-path

    # Clean up generated .class files.
    rm FizzBuzz.class FizzBuzzTest.class
    exit 0
fi

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