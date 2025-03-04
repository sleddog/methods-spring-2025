#!/bin/bash

if [ -z "$1" ]; then
	python ./main.py
else
	python ./main.py "$1"

fi 
