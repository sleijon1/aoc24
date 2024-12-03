#!/bin/bash

# Loop through numbers 3 to 25
for i in {3..25}
do
    # Create directory named d<i>
    mkdir -p d$i
    
    # Create input.txt file in the directory
    touch d$i/input.txt
    
    # Create d3.py file in the directory (adjusting the name to be d<i>.py)
    touch d$i/d$i.py
    
    echo "Created directory and files for d$i"
done

echo "All folders and files have been created."
