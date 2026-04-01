#!/bin/bash
# setup_env.sh - Configure workflow tool aliases on this machine
# Run this script after cloning workflow-tools on a new machine.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SAVE_WORK_PATH="$SCRIPT_DIR/save_work.py"
INIT_PLANS_PATH="$SCRIPT_DIR/init_plans.py"
SYNC_REPOS_PATH="$SCRIPT_DIR/sync_repos.py"

# Determine shell config file
if [ -f "$HOME/.bashrc" ]; then
    SHELL_RC="$HOME/.bashrc"
elif [ -f "$HOME/.zshrc" ]; then
    SHELL_RC="$HOME/.zshrc"
else
    SHELL_RC="$HOME/.bashrc"
fi

echo "Setting up workflow tool aliases in $SHELL_RC..."

# Marker to identify our block
MARKER="# -- workflow-tools aliases --"

# Remove old block if present
if grep -q "$MARKER" "$SHELL_RC" 2>/dev/null; then
    echo "Removing existing workflow-tools aliases..."
    sed -i '' "/$MARKER/,/$MARKER/d" "$SHELL_RC"
fi

# Append new aliases
cat >> "$SHELL_RC" << EOF
$MARKER
alias save_work='python3 $SAVE_WORK_PATH'
alias init_plans='python3 $INIT_PLANS_PATH'
alias sync_repos='python3 $SYNC_REPOS_PATH'
$MARKER
EOF

echo "Aliases added:"
echo "  save_work  -> python3 $SAVE_WORK_PATH"
echo "  init_plans -> python3 $INIT_PLANS_PATH"
echo "  sync_repos -> python3 $SYNC_REPOS_PATH"
echo ""
echo "Run 'source $SHELL_RC' or open a new terminal to activate."
