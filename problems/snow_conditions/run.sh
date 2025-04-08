#!/bin/bash

if [ -z "$1" ]; then
	python3 ./main.py
else
	python3 ./main.py "$1"

fi 
