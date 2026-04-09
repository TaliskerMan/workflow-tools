#!/bin/bash
# Commits changes in all repos that have uncommitted changes

BASE_DIR="${2:-/home/freecode/antigrav}"
COMMIT_MSG="${1:-Auto-commit at $(date '+%Y-%m-%d %H:%M:%S')}"

echo "Checking Git repositories in $BASE_DIR for uncommitted changes..."
echo "Commit message to be used: '$COMMIT_MSG'"
echo "----------------------------------------"

find "$BASE_DIR" -maxdepth 2 -type d -name ".git" 2>/dev/null | sort | while read gitdir; do
    repo=$(dirname "$gitdir")
    
    # Change into the repository directory
    cd "$repo" || continue
    
    # Check if there are any uncommitted changes (both tracked and untracked)
    if [ -n "$(git status --porcelain)" ]; then
        echo "--> Committing changes in $repo"
        git add .
        git commit -S -m "$COMMIT_MSG"
    else
        echo "    No changes to commit in $repo"
    fi
done

echo "----------------------------------------"
echo "Done."
