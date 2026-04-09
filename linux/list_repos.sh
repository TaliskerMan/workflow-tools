#!/bin/bash
# Lists all git repositories in the base directory

BASE_DIR="${1:-/home/freecode/antigrav}"

echo "Listing Git repositories in $BASE_DIR..."
echo "----------------------------------------"

# Find all directories named '.git' and print their parent directory
find "$BASE_DIR" -maxdepth 2 -type d -name ".git" 2>/dev/null | sort | while read gitdir; do
    repo=$(dirname "$gitdir")
    echo "- $repo"
done
echo "----------------------------------------"
echo "Done."
