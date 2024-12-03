#!/bin/bash

# Navigate to the 'days' folder
cd days || { echo "The 'days' folder does not exist. Exiting."; exit 1; }

# Loop through each d(x) folder
for i in {1..25}
do
    # Check if the Python file exists inside the directory
    if [ -f d$i/d$i.py ]; then
        # Append the line to the Python file
        echo 'lines = open("input.txt").read().splitlines()' >> d$i/d$i.py
        echo "Added line to d$i/d$i.py"
    else
        echo "Python file d$i/d$i.py does not exist. Skipping."
    fi
done

echo "All applicable Python files have been updated."
