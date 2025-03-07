#!/bin/bash
regex=""
while IFS= read -r item; do
  # Escape any regex special characters in the item
  escaped_item=$(echo "$item" | sed 's/[.^$*+?()[\]{}|]/\\&/g')
  regex+="$escaped_item|"
done < "$1"

# Remove the trailing pipe
regex=${regex%|}
#echo $regex

zcat $2 | 
  grep -E "${regex::-1}" | 
  grep -E "TMAX" | 
  cut -d, -f1,2,4 | 
  cut --complement -c17-20 |
  python3 yearly_median.py
