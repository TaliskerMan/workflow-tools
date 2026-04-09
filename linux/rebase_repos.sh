#!/bin/bash
# Rebases all repos against their remote tracking branches

BASE_DIR="${1:-/home/freecode/antigrav}"

echo "Rebasing Git repositories in $BASE_DIR against origin..."
echo "----------------------------------------"

find "$BASE_DIR" -maxdepth 2 -type d -name ".git" 2>/dev/null | sort | while read gitdir; do
    repo=$(dirname "$gitdir")
    
    echo "--> Processing $repo"
    cd "$repo" || continue
    
    current_branch=$(git branch --show-current)
    if [ -n "$current_branch" ]; then
        echo "    Active branch: $current_branch"
        
        # Fetch latest remotes in the background or quietly
        echo "    Fetching remotes..."
        git fetch --all --quiet
        
        # Rebase against the tracked remote branch
        echo "    Rebasing on origin/$current_branch..."
        git rebase "origin/$current_branch"
        
        if [ $? -ne 0 ]; then
            echo "    [!] Rebase encountered conflicts or an error. Aborting rebase."
            git rebase --abort
        fi
    else
        echo "    Not currently on any branch (detached HEAD or empty). Skipping rebase."
    fi
    echo ""
done

echo "----------------------------------------"
echo "Done."
