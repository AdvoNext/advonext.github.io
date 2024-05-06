#!/bin/zsh

# Check if the required parameters are provided
if [ "$#" -ne 3 ]; then
  echo "Usage: $0 <file_path> <line_number> <text>"
  exit 1
fi

# The file to insert text into
file="$1"

# The line number after which the text will be inserted
line_number="$2"

# The text to be inserted
new_text="$3"

# Check if the file exists
if [ ! -f "$file" ]; then
  echo "File not found: $file"
  exit 1
fi

# Check if the line number is invalid (less than 1)
if [ "$line_number" -lt 1 ]; then
  echo "Invalid line number: $line_number"
  exit 1
fi

# Line number cannot be greater than the number of lines in the file
num_lines=$(wc -l < "$file")
if [ "$line_number" -gt "$num_lines" ]; then
  echo "The line number ($line_number) is greater than the number of lines in the file ($num_lines)"
  exit 1
fi

# Copy lines from 1 to the desired line into a temporary file
head -n "$line_number" "$file" > temp_file

# Insert the new text into the temporary file
echo "$new_text" >> temp_file

# Copy the remaining lines into the temporary file
tail -n +"$((line_number + 1))" "$file" >> temp_file

# Move the temporary file to the original file
mv temp_file "$file"

echo "Text successfully inserted."
