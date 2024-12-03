#!/bin/bash

# Create the 'days' folder if it doesn't exist
mkdir -p days

# Loop through directories d3 to d25 and move them into 'days'
for i in {1..25}
do
    # Check if the directory exists
    if [ -d d$i ]; then
        mv d$i days/
        echo "Moved d$i to the 'days' folder."
    else
        echo "Directory d$i does not exist. Skipping."
    fi
done

echo "All directories have been moved into the 'days' folder."
