#!/usr/bin/env python3
import os
import subprocess
import datetime
import sys

def get_repo_root():
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        print("Error: Not inside a git repository.")
        sys.exit(1)

def find_plan_file(repo_root):
    repo_name = os.path.basename(repo_root)
    plan_file = os.path.join(repo_root, "plan", f"{repo_name}Plan.md")
    if os.path.exists(plan_file):
        return plan_file
    return None

def main():
    repo_root = get_repo_root()
    plan_file = find_plan_file(repo_root)
    
    if not plan_file:
        print(f"Error: Plan file not found in {repo_root}/plan/")
        print("Please run init_plans.py first or create it manually.")
        sys.exit(1)
        
    print(f"Updating plan: {plan_file}")
    
    # Get user input
    status = input("What did you accomplish? (Press Enter to finish): ")
    if not status:
        print("Aborted.")
        sys.exit(0)
        
    next_steps = input("What are the next steps? ")
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Append to plan file
    with open(plan_file, "a") as f:
        f.write(f"\n### {timestamp}\n")
        f.write(f"**Completed**: {status}\n")
        if next_steps:
            f.write(f"**Next Steps**: {next_steps}\n")
            
    print("Plan updated.")
    
    # Commit and push
    try:
        subprocess.run(["git", "add", plan_file], check=True, cwd=repo_root)
        commit_msg = f"Update plan: {timestamp}"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True, cwd=repo_root)
        print("Changes committed.")
        
        push = input("Push to GitHub? (Y/n): ").lower()
        if push != 'n':
            subprocess.run(["git", "push"], check=True, cwd=repo_root)
            print("Changes pushed to GitHub.")
            
    except subprocess.CalledProcessError as e:
        print(f"Error during git operation: {e}")

if __name__ == "__main__":
    main()
