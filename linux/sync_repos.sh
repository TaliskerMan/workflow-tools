#!/bin/bash
# Pulls from remote and then pushes local commits for all repos

BASE_DIR="${1:-/home/freecode/antigrav}"

echo "Syncing (pull & push) Git repositories in $BASE_DIR..."
echo "----------------------------------------"

find "$BASE_DIR" -maxdepth 2 -type d -name ".git" 2>/dev/null | sort | while read gitdir; do
    repo=$(dirname "$gitdir")
    
    echo "--> Syncing $repo"
    cd "$repo" || continue
    
    current_branch=$(git branch --show-current)
    if [ -n "$current_branch" ]; then
        echo "    Active branch: $current_branch"
        
        # Pull updates
        echo "    Pulling from origin..."
        git pull origin "$current_branch"
        
        # Push local changes
        echo "    Pushing to origin..."
        git push origin "$current_branch"
    else
        echo "    Not currently on any branch (detached HEAD or empty). Skipping sync."
    fi
    echo ""
done

echo "----------------------------------------"
echo "Done."
