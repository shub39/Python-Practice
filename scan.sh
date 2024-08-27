#!/bin/bash

# Simple Shell script to make markdown table

BASE_FOLDER="PCC-DS-391"

dirs=($(ls -d "$BASE_FOLDER"/*/))

max_files=0
for dir in "${dirs[@]}"; do
  file_count=$(ls "$dir" | wc -l)
  if [ "$file_count" -gt "$max_files" ]; then
    max_files=$file_count
  fi
done

echo -n "|"
for dir in "${dirs[@]}"; do
  dirname=$(basename "$dir")
  echo -n " $dirname |"
done
echo

echo -n "|"
for dir in "${dirs[@]}"; do
  echo -n " --------- |"
done
echo

for ((i = 1; i <= max_files; i++)); do
  echo -n "|"
  for dir in "${dirs[@]}"; do
    file=$(ls "$dir" | sort -V | sed -n "${i}p")
    if [ -n "$file" ]; then
      dir_basename=$(basename "$dir")
      echo -n " [$file]($BASE_FOLDER/$dir_basename/$file) |"
    else
      echo -n " |"
    fi
  done
  echo
done
