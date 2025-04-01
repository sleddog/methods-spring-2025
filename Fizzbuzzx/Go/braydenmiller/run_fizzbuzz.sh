if [ $# -eq 0 ]; then
  echo "Usage: ./run_fizzbuzz.sh <number>"
  exit 1
fi

go run Fizzbuzz.go "$1"