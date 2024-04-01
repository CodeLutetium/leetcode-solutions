#!/bin/bash

n=$1

# Search for file starting with the number n
file=$(find . -type f -name "${n}*" -print -quit)

if [ -z "$file" ]; then
    echo "No file starting with $n found."
else
    # Perform git add on the file
    git add "$file"


    # Get the filename without the extension
    filename=$(basename "$file")
    filename="${filename%.*}"

    git commit -m "Added $filemname"
    git push
    echo "Added $file to git."
fi